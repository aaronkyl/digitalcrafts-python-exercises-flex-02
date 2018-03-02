madlib = "The {adj} cat {verb} on the {noun} {adv}"

print("Fill in the blanks!")
print(madlib.format(adj="__(adj)__", verb="__(verb)__", noun="__(noun)__", adv="__(adv)__"))

adj1 = input("Give me an adjective: ")
verb1 = input("Give me a verb: ")
noun1 = input("Give me a noun: ")
adv1 = input("Give me an adverb: ")

print(madlib.format(adj=adj1, verb=verb1, noun=noun1, adv=adv1))