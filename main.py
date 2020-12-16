import export, source
import getpass

def main():
    group_id = input("input group id:")
    access_token = getpass.getpass("input access_token:")
    print("wait pls...")
    vkapi = source.VkSource(v="5.126")
    csv = export.CSVExport(vkapi, 100)
    csv.export(group_id, access_token)
    csv.dispose()
    print("done!")

if __name__ == "__main__":
    main()