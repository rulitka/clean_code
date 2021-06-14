// Примеры правильного именования при перегрузке конструкторов с использованием статических метод-фабрик с именами, описывающими аргументы.
1. Foo foo = new Foo() - Foo foo = Foo.createWithBar()
2. Test t = new Test() - Test t = Test.getObject()
3. Vinoth vin = new Vinoth() - Vinoth vin = Vinoth.createObject()
4. Coordinate c = Coordinate.createFromCartesian(double x, double y)
5. Coordinate c = Coordinate.createFromPolar(double distance, double angle)
