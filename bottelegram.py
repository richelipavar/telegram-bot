import telebot

CHAVE_API = "5308713510:AAEArlzkT8Aj3WS8BtyZy9S2zAdiivMtFts"

bot = telebot.TeleBot(CHAVE_API)

#mensagem cardápio

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza para a sua casa: Tempo de espera em 25 a 30 minutos")

@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o hambpurguer para a sua casa: Tempo de espera em 20 a 25 minutos")

@bot.message_handler(commands=["salada"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a salada para a sua casa: Tempo de espera em 15 a 20 minutos")

#opções disponíveis

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Escolha o que deseja (Clique em uma opção)
    /pizza Pizza
    /hamburguer Hambúrguer
    /salada Salada"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para eviar uma reclamação, mande um e-mail para reclamacao@contato.com")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Obrigado! O chef mandou um abraço de volta")


def verificar(mensagem):
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
        /opcao1 Fazer um pedido
        /opcao2 Reclamar de um pedido
        /opcao3 Mandar um abraço ao chef do restaurante
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()