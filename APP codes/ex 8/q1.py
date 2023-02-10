from pyDatalog import pyDatalog


pyDatalog.create_terms(
    "Bear, Elephant, Cat, Gray, Brown, Big, Small, size, color, X, Dark")

+size("Bear", "Big")
+size("Elephant", "Big")
+size("Cat", "Small")
+color("Bear", "Brown")
+color("Cat", "Black")
+color("Elephant", "Gray")
Dark(X) <= (color(X, "Black"))
Dark(X) <= (color(X, "Brown"))

print(Dark(X) & (size(X, "Big")))
