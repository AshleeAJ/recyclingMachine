class Container:

    def __init__(self, material, value):
        self.material = material
        self.value = value

# Hardcoded containers
plastic = Container("plastic", 0.50)
glass = Container("glass", 1.00)
cardboard = Container("cardboard", 0.10)
tin = Container("tin", 0.20)
