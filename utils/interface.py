FILTER_CHOICES = {
    "CATEGORIES" : ("Todas as categorias", "Hatchback", "Sedan", "SUV", "Pick-Up", "Eletric"),
    "BRANDS" : ("Todas as marcas", "Audi",  "BMW", "BYD", "Chevrolet", "Fiat", "Ford", "Honda", "Hyundai", "Jeep", "Mercedes", "Nissan",  "Toyota", "Volkswagen"),
    "PRICES_PER_DAY" : ("Sem limite", "$200", "$300", "$500", "$800", "$1000"),
    "YEAR" : ("Todos os anos", "2020", "2021", "2022", "2023", "2024", "2025", "2026")
}

TREEVIEW_COLUMNS = ["ID", "Modelo", "Ano", "Placa", "Combustível", "Categoria", "Marca", "Transmissão", "Preço base p/dia (R$)"]

FORM_CHOICES = {
    "CATEGORIES" : ("Hatchback", "Sedan", "SUV", "Pick-Up", "Eletric"),
    "BRANDS" : ("Audi",  "BMW", "BYD", "Chevrolet", "Fiat", "Ford", "Honda", "Hyundai", "Jeep", "Mercedes", "Nissan", "Toyota", "Volkswagen"),
    "FUEL" : ("Gas", "Disel", "Flex", "Eletric"),
    "TRANSMISSION" : ("Manual", "Automatic")
}

WEIGHT_OPTIONS = {
    "CATEGORIES" : {
        "Hatchback" : 1,
        "Sedan" : 1.5,
        "SUV" : 3,
        "Pick-Up" : 5,
        "Eletric" : 8
    },
    "BRANDS" : {
        "Toyota" : 10,
        "BYD" : 70,
        "Jeep" : 40,
        "Ford" : 5,
        "Fiat" : 10,
        "Chevrolet" : 15,
        "Honda" : 15,
        "Nissan" : 30,
        "BMW" : 80,
        "Audi" : 80,
        "Mercedes" : 70,
        "Volkswagen" : 10,
        "Hyundai" : 15
    },
    "FUEL" : {
        "Gas" : 10,
        "Disel" : 25,
        "Flex" : 30,
        "Eletric" : 50
    },
    "TRANSMISSION" : {
        "Manual" : 5,
        "Automatic" : 15
    }
}