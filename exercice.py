#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_even_keys(dictionary):
	#Extraire les cles
	even_keys = {k for k, v in dictionary.items() if k % 2 == 0}

	#Extraire les cles paires
	#if yeet.keys()%2:

	return even_keys

def join_dictionaries(dictionaries):
	# result= {}
	# for d in dictionaries:
	# 	for key, value in d.items():
	# 		result = (key, value)
	# 		print(result)
	# return result

	#return {**dictionaries[0], dictionaries[1]} #seulement si on sait on a 2 items
	return {key: value
				for d in dictionaries
					for key, value in d.items()}

def dictionary_from_lists(keys, values):
	# result= {}
	# for i in range(min(len(keys), len(values))):
	# 	result[keys[i]] = values[i]
	# return result

	# return{keys[i]: values[i] for i in range(min(len(keys), len(values)))}
	return dict(zip(keys, values))

def get_greatest_values(dictionary, num_values):
	# #Extraire les valeurs
	# #values={v for k, v in dictionary.items()}
	# values=dictionary.values()
	# #Ordonner les valeurs a l'envers
	# sorted_values = sorted(values, reverse=True)
	# #Choisir les nym_values plus grands
	# return list(sorted_values[0:num_values])
	return list(sorted(dictionary.values(), reverse=True)[0:num_values]) #le list est optionel pcq ca retourne une liste de tte facon

def get_sum_values_from_key(dictionaries, key):
	#Extraire les valeurs assoicees a une cle
	#Faire la somme des valeurs
	# sum = 0
	# for d in dictionaries:
	# 	if key in d:
	# 		sum += d[key]

	# values = []
	# for d in dictionaries:
	# 	if key in d:
	# 		values.append(d[key])
	# return sum(values)

	return sum([d[key] for d in dictionaries if key in d])


if __name__ == "__main__":
	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	print(get_even_keys(yeet))
	print()

	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	doot = {
		0xBEEF: "doot",
		0xDEAD: "DOOT",
		0xBABE: "dOoT"
	}
	print(join_dictionaries([yeet, doot]))
	print()
	
	doh = [
		"D'OH!",
		"d'oh",
		"DOH!"
	]
	nice = [
		"NICE!",
		"nice",
		"nIcE",
		"NAIIIIICE!"
	]
	print(dictionary_from_lists(doh, nice))
	print()
	
	nums = {
		"nice": 69,
		"nice bro": 69420,
		"AGH!": 9000,
		"dude": 420,
		"git gud": 1337
	}
	print(get_greatest_values(nums, 1))
	print(get_greatest_values(nums, 3))
	print()

	bro1 = {
		"money": 12,
		"problems": 14,
		"trivago": 1
	}
	bro2 = {
		"money": 56,
		"problems": 406
	}
	bro3 = {
		"money": 1,
		"chichis": 1,
		"power-level": 9000
	}
	print(get_sum_values_from_key([bro1, bro2, bro3], "problems"))
	print(get_sum_values_from_key([bro1, bro2, bro3], "money"))
	print()

	#pratique de zip
	a = ("a", "b", "c")
	b = ("d", "e", "f")
	c = ("g", "h", "i")
