from telebot import types
import telebot

#remove, about, replacement
key1 = telebot.types.ReplyKeyboardMarkup(True, True, True)
key1.row('remove', 'about', 'replacement')

#continue
key2 = telebot.types.ReplyKeyboardMarkup(True)
key2.row('continue')

#change, begin, help, send, info
key3 = telebot.types.ReplyKeyboardMarkup(True, True, True, True)
key3.row('change', 'begin', 'help', 'send', 'info')

#registration
key4 = telebot.types.ReplyKeyboardMarkup(True)
key4.row('registration')

#registration, help
key5 = telebot.types.ReplyKeyboardMarkup(True, True)
key5.row('registration', 'help')

#replacement, remove
key6 = telebot.types.ReplyKeyboardMarkup(True, True, True)
key6.row('replacement', 'remove', 'info')

#replacement
key7 = telebot.types.ReplyKeyboardMarkup(True, True)
key7.row('replacement', 'info')

#change
key8 = telebot.types.ReplyKeyboardMarkup(True)
key8.row('change')




