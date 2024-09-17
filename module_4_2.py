def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов inner_function внутри test_function
    inner_function()

# Вызов test_function, который в свою очередь вызовет inner_function
test_function()

# Попробуем вызвать inner_function вне test_function
inner_function()