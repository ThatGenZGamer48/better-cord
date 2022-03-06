import discord
from discord.ext import commands
from typing import Union

class BetterCord:
    # TODO: Add discord.Bot too.
    def __init__(self, pycord_bot: commands.Bot, developer_mode: bool = False, help_type: list = "embed"):
        self.pycord_bot: commands.Bot = pycord_bot
        self.developer_mode: bool = developer_mode
        self.help_type: list = help_type
        
    def create_help_embed(self, embed_title: str = None, embed_colour: discord.Colour = None):
        cog_names = [cog for cog in self.pycord_bot.cogs]
        
        emb_title = "Help"
        emb_colour = discord.Colour.og_blurple()
        
        if embed_title:
            emb_title = embed_title
            
        if emb_color:
            emb_colour = embed_colour
        
        embed = discord.Embed(
            title=emb_title,
            colour=emb_colour,
            timestamp=discord.utils.utcnow()
        )
        
        for cog_name in cog_names:
            commands = []

            for command in self.pycord_bot.get_cog(cog_name).walk_commands():
                commands.append(f'`{command.name}`')

            command_list = ", ".join(commands)

            embed.add_field(name=cog_name, value=command_list, inline=False)

        return embed
        
