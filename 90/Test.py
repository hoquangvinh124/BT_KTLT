import xml.etree.ElementTree as ET

def parse_groups(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    groups = []
    for g in root.findall('group'):
        gid = g.find('id').text.strip()
        gname = g.find('name').text.strip()
        groups.append({"id": gid, "name": gname})
    return groups

def parse_devices(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    devices = []
    for d in root.findall('device'):
        group_id = d.attrib.get('groupid', '').strip()
        dev_id = d.find('id').text.strip()
        dev_name = d.find('name').text.strip()
        devices.append({
            "groupid": group_id,
            "id": dev_id,
            "name": dev_name
        })
    return devices

def display_devices_by_group(groups, devices):
    print("=== List Device Belong To Group ===")
    for group in groups:
        print(f"\nGroup {group['id']} - {group['name']}:")
        count = 0
        for dev in devices:
            if dev['groupid'] == group['id']:
                print(f"  - Device ID: {dev['id']}, Name: {dev['name']}")
                count += 1


def filter_devices_by_group(groups, devices, input_gid):
    group_name = None
    for g in groups:
        if g['id'] == input_gid:
            group_name = g['name']
            break
    if group_name is None:
        print(f"Group ID {input_gid} not exits!")
        return
    print(f"=== Device list for group {input_gid} - {group_name} ===")
    count = 0
    for dev in devices:
        if dev['groupid'] == input_gid:
            print(f"  - Device ID: {dev['id']}, Name: {dev['name']}")
            count += 1


def print_group_with_most_devices(groups, devices):
    max_count = 0
    max_group = None
    for group in groups:
        count = sum(1 for d in devices if d['groupid'] == group['id'])
        if count > max_count:
            max_count = count
            max_group = group
    if max_group:
        print(f"\nGroup with most device: {max_group['id']} - {max_group['name']}")
        print(f"Quantity = {max_count}")

def main():
    groups_xml = "groups.xml"
    groups = parse_groups(groups_xml)

    devices_xml = "devices.xml"
    devices = parse_devices(devices_xml)

    display_devices_by_group(groups, devices)

    print("\n--- Filter Device By Group ID ---")
    input_gid = input("Enter group id (ex: g1, g2, g3): ")
    filter_devices_by_group(groups, devices, input_gid)

    print_group_with_most_devices(groups, devices)

main()