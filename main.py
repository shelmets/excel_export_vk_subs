import export, source

def main():
    print("wait pls...")
    access_token = "472e1787472e1787472e1787ec474e0a994472e472e178718f430a6a31e6db38933835e"
    vkapi = source.VkSource(v="5.126")
    csv = export.CSVExport(vkapi, 100)
    csv.export("198006443", access_token)
    csv.dispose()
    print("done!")

if __name__ == "__main__":
    main()