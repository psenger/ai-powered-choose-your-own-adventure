import configparser


def load_graph_from_ini(filename='data.ini') -> dict:
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


def escape_mermaid_text(text):
    """Escape special characters for mermaid"""
    # In mermaid, quotes need to be escaped
    return text.replace('"', '&quot;')


def generate_mermaid_graph(graph_data):
    """Generate mermaid graph syntax from the graph data"""
    lines = []
    lines.append("```mermaid")
    lines.append("graph TD")

    # First, define all nodes with their titles and rewards
    for node_id, node_data in graph_data.items():
        title = escape_mermaid_text(node_data['title'])

        # Add reward info to the node if it exists
        if node_data['item_reward']:
            node_label = f'{node_id}["{title}<br/>reward: {node_data["item_reward"]}"]'
        else:
            node_label = f'{node_id}["{title}"]'

        lines.append(f"    {node_label}")

    lines.append("")  # Empty line for readability

    # Then, define all connections with requirements
    for node_id, node_data in graph_data.items():
        for connection in node_data['connections']:
            if connection in graph_data:  # Validate connection exists
                # Check if the target node has requirements
                target_node = graph_data[connection]
                required_items = target_node['requires_items']

                if required_items:
                    # Show required items on the arrow
                    items_str = ','.join(required_items)
                    lines.append(f'    {node_id} -->|"{items_str}"| {connection}')
                else:
                    lines.append(f'    {node_id} --> {connection}')

    lines.append("```")

    return '\n'.join(lines)


def update_readme_with_mermaid(readme_file='README.md', graph_data=None):
    """Read README.md, find and replace the mermaid code block"""

    # Generate the new mermaid graph
    new_mermaid = generate_mermaid_graph(graph_data)

    # Read the current README content
    try:
        with open(readme_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {readme_file} not found!")
        return False

    # Find the mermaid code block using simple string methods
    start_marker = '```mermaid'
    end_marker = '```'

    # Find where the mermaid block starts
    start_pos = content.find(start_marker)
    if start_pos == -1:
        print(f"Error: No mermaid code block found in {readme_file}")
        return False

    # Find where it ends (the next ``` after the start)
    # We need to search after the start_marker
    search_from = start_pos + len(start_marker)
    end_pos = content.find(end_marker, search_from)
    if end_pos == -1:
        print(f"Error: Mermaid code block not properly closed in {readme_file}")
        return False

    # Include the closing ``` in our range
    end_pos = end_pos + len(end_marker)

    # Replace the old mermaid block with the new one
    new_content = content[:start_pos] + new_mermaid + content[end_pos:]

    # Write back to README
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Successfully updated {readme_file} with new mermaid graph!")
    return True


def validate_graph(graph_data):
    """Validate the graph structure and report any issues"""
    issues = []

    for node_id, node_data in graph_data.items():
        # Check if all connections exist
        for connection in node_data['connections']:
            if connection not in graph_data:
                issues.append(f"Node '{node_id}' has invalid connection to '{connection}'")

        # Check if required items are reasonable (optional validation)
        if node_data['requires_items']:
            # Collect all possible item rewards
            all_rewards = set()
            for n_id, n_data in graph_data.items():
                if n_data['item_reward']:
                    all_rewards.add(n_data['item_reward'])

            # Check if required items can be obtained
            for req_item in node_data['requires_items']:
                if req_item not in all_rewards:
                    issues.append(f"Node '{node_id}' requires '{req_item}' but it's not rewarded anywhere")

    if issues:
        print("Graph validation issues found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("Graph validation passed!")

    return len(issues) == 0


def main():
    """Main function to update the README with mermaid graph"""

    # Load the graph data
    print("Loading graph from data.ini...")
    graph = load_graph_from_ini('../data.ini')

    # Display loaded graph info
    print(f"Loaded {len(graph)} nodes from data.ini")

    # Validate the graph
    print("\nValidating graph structure...")
    is_valid = validate_graph(graph)

    if not is_valid:
        response = input("\nGraph has validation issues. Continue anyway? (y/n): ")
        if response.lower() != 'y':
            print("Aborted.")
            return

    # Update the README
    print("\nUpdating README.md with new mermaid graph...")
    success = update_readme_with_mermaid('../README.md', graph)

    if success:
        print("\nDone! The mermaid graph in README.md has been updated.")

        # Optional: Show summary
        print("\nGraph Summary:")
        print(f"  - Total nodes: {len(graph)}")

        # Count nodes with rewards
        reward_nodes = sum(1 for n in graph.values() if n['item_reward'])
        print(f"  - Nodes with rewards: {reward_nodes}")

        # Count total connections
        total_connections = sum(len(n['connections']) for n in graph.values())
        print(f"  - Total connections: {total_connections}")

        # Find start and end nodes
        start_nodes = [nid for nid, n in graph.items() if not n['requires_items'] and n['connections']]
        end_nodes = [nid for nid, n in graph.items() if not n['connections']]

        print(f"  - Start nodes: {', '.join(start_nodes)}")
        print(f"  - End nodes: {', '.join(end_nodes)}")


if __name__ == "__main__":
    main()