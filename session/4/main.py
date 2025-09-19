import configparser


def load_graph_from_ini(filename='data.ini') -> dict:

    config = configparser.ConfigParser()
    config.read(filename)
    data = {}

    for section in config.sections():
        single_node_data = {
            'story_key': section,
            'title': config.get(section, 'title'),
            'requires_items': [item.strip() for item in config.get(section, 'requires_items').split(',') if item.strip()],
            'connections': [conn.strip() for conn in config.get(section, 'connections').split(',') if conn.strip()],
            'item_reward': config.get(section, 'item_reward') if config.get(section, 'item_reward') != 'None' else None,
        }
        data[section] = single_node_data

    return data

def load_stories(filename='stories.ini') -> dict:
    config = configparser.ConfigParser()
    config.read(filename)

    data = {}

    for section in config.sections():
        single_node_data = {
            'story': config.get(section, 'story')
        }
        data[section] = single_node_data

    return data

if __name__ == "__main__":

    graph = load_graph_from_ini()
    stories = load_stories()

    print("=" * 50)
    print("Adventure Game Graph:")
    print("=" * 50)

    for node_id, node_data in graph.items():
        print(f"\nNode: {node_id}")
        print(f"  Title: {node_data['title']}")
        print(f"  Required Items: {node_data['requires_items']}")
        print(f"  Connections: {node_data['connections']}")
        print(f"  Item Reward: {node_data['item_reward']}")

    print("=" * 50)
    print("Stories:")
    print("=" * 50)

    for node_id, node_data in stories.items():
        print(f"\nNode: {node_id}")
        print(f"Story: {node_data['story']}")