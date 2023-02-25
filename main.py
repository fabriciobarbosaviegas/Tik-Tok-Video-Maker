from robots.text import write_script


def main():
    api_key = input("Open AI Api Key:")
    theme = input("Video Theme: ")

    write_script(api_key, theme)



if __name__ == "__main__":
    main()