from discord.ext import commands
import discord
import random
# Permisos por defecto
intents = discord.Intents.default()

# Permitimos que el bot lea el contenido de los mensajes
intents.message_content = True

# Creamos el bot con prefijo -
bot = commands.Bot(command_prefix='-', intents=intents)


@bot.event
async def on_ready():

    print(f'Tu bot {bot.user} está en línea')
    print(f'ID del bot: {bot.user.id}')



@bot.command()
async def hola(ctx):

    await ctx.send(f'Hola {ctx.author.mention} 👋')


@bot.command()
async def despedirse(ctx, *, mensaje: str):

    mensaje = mensaje.lower().strip()

    if 'bye' in mensaje:

        await ctx.send('Goodbye 👋')

    elif 'hastaluego' in mensaje:

        await ctx.send('Hasta nunca 😭')

    else:

        await ctx.send('Todo bien, cuídese 👍')



@bot.command()
async def ayuda(ctx):

    await ctx.send(
        '**📖 Comandos disponibles:**\n\n'
        '`-hola` → El bot te saluda.\n'
        '`-despedirse <mensaje>` → El bot responde a tu despedida.\n'
        '`-ping` → Comprueba la conexión del bot.\n'
        '`-info` → Muestra información sobre el servidor.\n'
        '`-usuario` → Muestra información sobre ti.\n'
        '`-ayuda` → Muestra esta lista.'
    )



@bot.command()
async def ping(ctx):

    latencia = round(bot.latency * 1000)

    await ctx.send(f'🏓 Pong! `{latencia} ms`')


@bot.command()
async def info(ctx):

    servidor = ctx.guild

    await ctx.send(
        f'**📋 Información del servidor**\n\n'
        f'🏠 Nombre: `{servidor.name}`\n'
        f'👥 Miembros: `{servidor.member_count}`\n'
        f'🆔 ID: `{servidor.id}`'
    )


@bot.command()
async def usuario(ctx):

    usuario = ctx.author

    await ctx.send(
        f'**👤 Información del usuario**\n\n'
        f'Nombre: `{usuario.name}`\n'
        f'ID: `{usuario.id}`\n'
        f'Cuenta creada: `{usuario.created_at.strftime("%d/%m/%Y")}`'
    )



@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.CommandNotFound):

        await ctx.send(
            '❌ Ese comando no existe. Usa `-ayuda` para ver los comandos.'
        )

    elif isinstance(error, commands.MissingRequiredArgument):

        await ctx.send(
            '❌ Te falta escribir un argumento para usar este comando.'
        )

    else:

        print(f'Error: {error}')


@bot.command()
async def mem(ctx):
    with open('imagenes/006a00af-c8c5-46f6-b56f-794e17d1b485.jpeg.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)



@bot.command()
async def reto(ctx):
    # Creamos una lista con diferentes retos ecológicos
    retos = [
        ' Reto: Hoy separa correctamente todos los residuos de tu casa.',
        ' Reto: Evita usar botellas de plástico durante todo el día.',
        ' Reto: Reutiliza una bolsa en lugar de pedir una nueva.',
        ' Reto: Apaga las luces que no estés utilizando durante todo el día.',
        ' Reto: Busca una caja u objeto que puedas reutilizar en vez de botarlo.',
        ' Reto: Hoy intenta reducir el tiempo que pasas usando agua.',
        ' Reto: No desperdicies comida durante todo el día.',
        ' Reto: Recoge y separa correctamente los residuos de una habitación de tu casa.'
    ]
    # Elegimos un reto al azar de la lista
    reto_elegido = random.choice(retos)
    # Mostramos el reto elegido en el canal de Discord
    await ctx.send(f' **Tu reto ecológico de hoy:**\n\n{reto_elegido}')

@bot.command()
async def clasificar(ctx, residuo):
    residuo = residuo.lower()
    # Convertimos el residuo escrito a minúsculas

    # Lista de residuos orgánicos
    organico = ["cascara", "comida", "fruta", "verdura", "hojas"]
    # Lista de residuos reciclables
    reciclable = ["botella", "plastico", "carton", "papel", "lata"]
    # Lista de residuos que no son reciclables
    no_reciclable = ["pañal", "servilleta", "chicle"]

    if residuo in organico:
        await ctx.send(" Residuo orgánico. Colócalo en el contenedor de residuos orgánicos.")
    elif residuo in reciclable:
        await ctx.send(" Residuo reciclable. Colócalo en el contenedor de reciclaje.")
    elif residuo in no_reciclable:
        await ctx.send(" Residuo no reciclable. Colócalo en el contenedor de residuos comunes.")
    else:
        await ctx.send(" No conozco ese residuo. Intenta con otro.")


bot.run(token)