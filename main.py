name = "Austin"
nachname = "Powers"
alter = 38

# Varianten der formatierten Ausgabe
print("Hallo " + name, end="")
print(" Hallo %s %s, du bist %d Jahre alt" % (name, nachname, alter))
print("Hallo {} {}, fu bist {} Jahre alt ".format(name, nachname, alter))
print(f"Hallo {name} {nachname}, du bist {alter} Jahre alt")

