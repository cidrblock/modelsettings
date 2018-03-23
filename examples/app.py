from modelsettings import settings

def main():
    output = f"You ordered a {settings.SIZE} oz. cup of coffee"
    modifiers = []
    if settings.CREAM: modifiers.append("cream")
    if settings.SUGAR: modifiers.append("sugar")
    if modifiers:
        output += " with " + " and ".join(modifiers)
    output += "."
    print(output)

if __name__ == "__main__":
    main()
