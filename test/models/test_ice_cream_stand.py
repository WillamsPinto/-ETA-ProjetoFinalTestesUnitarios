from src.models.ice_cream_stand import IceCreamStand

class TestIceCreamStand:

    def test_flavors_available(self):
        #Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate', 'Morango', 'Baunilha', 'Laranja', 'Limão']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        exptected_message = "No momento temos os seguintes sabores de sorvete disponíveis:"

        #Act
        result = restaurant.flavors_available()

        #Asserts
        assert exptected_message == result[0]
        for index in range(1, result.__len__()):
            assert flavors_list.__contains__(result[index])

    def test_flavors_not_available(self):
        #Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = []
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        exptected_message = "Estamos sem estoque atualmente!"

        #Act
        result = restaurant.flavors_available()

        #Asserts
        assert exptected_message == result
        assert restaurant.flavors == flavors_list

    def test_find_flavor(self):
        # Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate', 'Morango', 'Baunilha', 'Laranja', 'Limão']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        expected_flavor = flavors_list[4]
        exptected_message = f"O sabor de {expected_flavor} está disponível!"

        # Act
        result = restaurant.find_flavor(expected_flavor)

        # Asserts
        assert result == exptected_message

    def test_not_find_flavor(self):
        # Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate', 'Morango', 'Baunilha', 'Laranja', 'Limão']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        find_flavor = "Tamarindo"
        exptected_message = f"Não temos no momento o sabor de {find_flavor}!"

        # Act
        result = restaurant.find_flavor(find_flavor)

        # Asserts
        assert result == exptected_message

    def test_find_flavor_no_stock(self):
            # Setup
            restaurant_name = "Sorveteria Lixo"
            restaurant_cuisine_type = "Sorveteria"
            flavors_list = []
            restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
            find_flavor = "Tamarindo"
            exptected_message = "Estamos sem estoque atualmente!"

            # Act
            result = restaurant.find_flavor(find_flavor)

            # Asserts
            assert result == exptected_message

    def test_add_flavor(self):
        # Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        new_flavor = "Tamarindo"
        exptected_message = f"{new_flavor} adicionado ao estoque!"

        # Act
        result = restaurant.add_flavor(new_flavor)

        # Asserts
        assert result == exptected_message
        assert restaurant.flavors.__contains__(new_flavor)

    def test_add_already_flavor(self):
        # Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        new_flavor = "Chocolate"
        expected_flavors_list_len = len(flavors_list)
        exptected_message = "Sabor já disponivel!"

        # Act
        result = restaurant.add_flavor(new_flavor)

        # Asserts
        assert result == exptected_message
        assert len(restaurant.flavors) == expected_flavors_list_len

    def test_add_None_flavor(self):
        # Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        new_flavor = None
        expected_flavors_list_len = len(flavors_list)
        exptected_message = "Sabor informado invalido!"

        # Act
        result = restaurant.add_flavor(new_flavor)

        # Asserts
        assert result == exptected_message
        assert len(restaurant.flavors) == expected_flavors_list_len

    def test_add_empty_flavor(self):
        # Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        new_flavor = ""
        expected_flavors_list_len = len(flavors_list)
        exptected_message = "Sabor informado invalido!"

        # Act
        result = restaurant.add_flavor(new_flavor)

        # Asserts
        assert result == exptected_message
        assert len(restaurant.flavors) == expected_flavors_list_len

    def test_add_flavor_invalid_type(self):
        # Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        new_flavor = 13246
        expected_flavors_list_len = len(flavors_list)
        exptected_message = "Sabor informado invalido!"

        # Act
        result = restaurant.add_flavor(new_flavor)

        # Asserts
        assert result == exptected_message
        assert len(restaurant.flavors) == expected_flavors_list_len