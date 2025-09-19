import configparser


def load_graph_from_ini(filename='data.ini'):
    """Load the adventure game graph from INI file"""
    config = configparser.ConfigParser()
    config.read(filename)

    data = {}

    for section in config.sections():
        single_node_data = {
            'title': config.get(section, 'title'),
            'requires_items': [item.strip() for item in config.get(section, 'requires_items').split(',') if
                               item.strip()],
            'connections': [conn.strip() for conn in config.get(section, 'connections').split(',') if conn.strip()],
            'item_reward': config.get(section, 'item_reward') if config.get(section, 'item_reward') != 'None' else None,
        }
        data[section] = single_node_data

    return data


def can_enter_node(node_data, inventory):
    """Check if we have all required items to enter a node"""
    required = node_data['requires_items']
    if not required:
        return True
    return all(item in inventory for item in required)


def find_all_paths(graph, start='start', end='victory'):
    """Find all valid paths from start to end node"""
    all_paths = []
    blocked_paths = []

    def dfs_path(current_node, target_node, visited, path, inventory):
        """Recursive depth-first search with inventory tracking"""

        # Add current node to path
        path.append(current_node)
        visited.add(current_node)

        # Collect item reward if available
        if graph[current_node]['item_reward']:
            item = graph[current_node]['item_reward']
            if item not in inventory:
                inventory.append(item)

        # Check if we reached the target
        if current_node == target_node:
            # Found a complete path!
            path_info = {
                'path': path.copy(),
                'final_inventory': inventory.copy()
            }
            all_paths.append(path_info)
        else:
            # Try all connections
            for next_node in graph[current_node]['connections']:
                if next_node not in visited:  # Avoid cycles
                    # Check if we can enter the next node
                    if can_enter_node(graph[next_node], inventory):
                        # Recursively explore
                        dfs_path(next_node, target_node, visited.copy(), path.copy(), inventory.copy())
                    else:
                        # Path blocked due to missing items
                        blocked_info = {
                            'partial_path': path.copy() + [f"✗ {next_node}"],
                            'blocked_at': next_node,
                            'missing_items': [item for item in graph[next_node]['requires_items'] if
                                              item not in inventory],
                            'current_inventory': inventory.copy()
                        }
                        blocked_paths.append(blocked_info)

    # Start the search
    dfs_path(start, end, set(), [], [])

    return all_paths, blocked_paths


def print_path_details(path_info, graph, path_num):
    """Print detailed information about a path"""
    path = path_info['path']
    inventory = []

    print(f"\n{'=' * 60}")
    print(f"PATH #{path_num}: Successfully reached Victory!")
    print(f"{'=' * 60}")
    print(f"Total steps: {len(path)}")

    for i, node in enumerate(path):
        node_data = graph[node]

        # Check requirements
        requires = node_data['requires_items']
        if requires:
            req_str = f" [requires: {', '.join(requires)}]"
        else:
            req_str = ""

        # Check reward
        if node_data['item_reward']:
            inventory.append(node_data['item_reward'])
            reward_str = f" → +{node_data['item_reward']}"
        else:
            reward_str = ""

        # Print step
        print(f"Step {i + 1}: {node_data['title']}{req_str}{reward_str}")

        # Show current inventory after this step
        if inventory:
            print(f"        Inventory: {', '.join(inventory)}")

    print(f"\nFinal inventory: {', '.join(path_info['final_inventory']) if path_info['final_inventory'] else 'None'}")


def print_blocked_paths(blocked_paths, graph):
    """Print information about blocked paths"""
    if not blocked_paths:
        return

    print(f"\n{'=' * 60}")
    print(f"BLOCKED PATHS: {len(blocked_paths)} paths couldn't reach Victory")
    print(f"{'=' * 60}")

    # Group blocked paths by what's blocking them
    blocking_summary = {}
    for blocked in blocked_paths:
        key = (blocked['blocked_at'], tuple(blocked['missing_items']))
        if key not in blocking_summary:
            blocking_summary[key] = []
        blocking_summary[key].append(blocked)

    for (blocked_node, missing_items), paths in blocking_summary.items():
        print(f"\n❌ Blocked at: {graph[blocked_node]['title']}")
        print(f"   Missing items: {', '.join(missing_items)}")
        print(f"   Number of paths blocked here: {len(paths)}")

        # Show a few example paths
        for i, blocked in enumerate(paths[:3]):  # Show max 3 examples
            path_str = " → ".join([graph[n]['title'] if '✗' not in n else n for n in blocked['partial_path'][:5]])
            if len(blocked['partial_path']) > 5:
                path_str += " → ..."
            print(f"   Example path {i + 1}: {path_str}")


def analyze_graph(graph):
    """Analyze the graph structure and item dependencies"""
    print("\n" + "=" * 60)
    print("GRAPH ANALYSIS")
    print("=" * 60)

    # Find all items in the game
    all_items = set()
    item_sources = {}
    item_requirements = {}

    for node_id, node_data in graph.items():
        if node_data['item_reward']:
            all_items.add(node_data['item_reward'])
            item_sources[node_data['item_reward']] = node_id

        for item in node_data['requires_items']:
            all_items.add(item)
            if item not in item_requirements:
                item_requirements[item] = []
            item_requirements[item].append(node_id)

    print(f"\nTotal items in game: {len(all_items)}")
    print("\nItem locations and usage:")

    for item in sorted(all_items):
        source = item_sources.get(item, "NOT FOUND IN GAME!")
        source_title = graph[source]['title'] if source != "NOT FOUND IN GAME!" else ""

        required_by = item_requirements.get(item, [])
        req_titles = [graph[n]['title'] for n in required_by]

        print(f"\n  {item}:")
        print(f"    Found at: {source_title if source_title else source}")
        if req_titles:
            print(f"    Required by: {', '.join(req_titles)}")
        else:
            print(f"    Required by: Not required anywhere")

    # Check for impossible items
    impossible_items = []
    for item in item_requirements:
        if item not in item_sources:
            impossible_items.append(item)

    if impossible_items:
        print(f"\n⚠️ WARNING: These items are required but never rewarded: {', '.join(impossible_items)}")


def main():
    """Main function to find all paths in the adventure game"""

    # Load the graph
    print("Loading adventure game from data.ini...")
    graph = load_graph_from_ini('../data.ini')

    print(f"Loaded {len(graph)} locations")

    # Analyze the graph structure
    analyze_graph(graph)

    # Find all paths
    print("\n" + "=" * 60)
    print("FINDING ALL PATHS FROM START TO VICTORY...")
    print("=" * 60)

    all_paths, blocked_paths = find_all_paths(graph)

    # Summary
    print(f"\n{'=' * 60}")
    print("SUMMARY")
    print(f"{'=' * 60}")
    print(f"✅ Found {len(all_paths)} valid path(s) to Victory!")
    print(f"❌ Found {len(blocked_paths)} blocked path attempt(s)")

    # Print successful paths
    if all_paths:
        print(f"\n{'=' * 60}")
        print("SUCCESSFUL PATHS TO VICTORY")
        print(f"{'=' * 60}")

        # Sort paths by length
        all_paths.sort(key=lambda x: len(x['path']))

        for i, path_info in enumerate(all_paths, 1):
            print_path_details(path_info, graph, i)
    else:
        print("\n⚠️ No valid paths found from start to victory!")
        print("This might mean the game is impossible to complete.")

    # Print blocked paths summary
    if blocked_paths:
        print_blocked_paths(blocked_paths, graph)

    # Final statistics
    print(f"\n{'=' * 60}")
    print("PATH STATISTICS")
    print(f"{'=' * 60}")

    if all_paths:
        path_lengths = [len(p['path']) for p in all_paths]
        print(f"Shortest path: {min(path_lengths)} steps")
        print(f"Longest path: {max(path_lengths)} steps")
        print(f"Average path length: {sum(path_lengths) / len(path_lengths):.1f} steps")

        # Find most collected items
        max_items = max(len(p['final_inventory']) for p in all_paths)
        print(f"Maximum items collected: {max_items}")


if __name__ == "__main__":
    main()