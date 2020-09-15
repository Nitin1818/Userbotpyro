from pyrogram import Client, filters


def user_mention(text):
    for i in text.split():
        if i.startswith("@"):
            return i[1:]


@Client.on_message(filters.me & filters.command(['ban'], ['.', '/']))
def ban_user(app, message):
    chat_type = message.chat.type
    stats = ("creator", "administrator")
    if chat_type != "private":
        if app.get_chat_member(message.chat.id, app.get_me().id).status in stats:
            if message.reply_to_message:
                if app.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status not in stats:
                    app.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, 0)
                    if message.reply_to_message.from_user.username:
                        message.edit(f'@{message.reply_to_message.from_user.username} is banned')
                        return
                    message.edit('[{}](tg://user?id={}) is banned'.format(
                        message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id
                    ), parse_mode="Markdown", disable_web_page_preview=True)
                    return
                message.edit('You can\'t ban admin')
                return
            if message.entities:
                if message.entities[0].type == 'mention':
                    if len(message.text.split()) == 2:
                        if app.get_chat_member(message.chat.id, user_mention(message.text)).status not in stats \
                                if user_mention(message.text) in\
                                   [i.user.username for i in app.iter_chat_members(message.chat.id)] else True:
                            app.kick_chat_member(message.chat.id, user_mention(message.text), 0)
                            message.edit(f'@{user_mention(message.text)} is banned')
                            return
                    else:
                        message.edit('You should use like this ".ban @username"')
                        return
                elif message.entities[0].type == 'text_mention':
                    if len(message.text.split()) == 2:
                        if app.get_chat_member(message.chat.id, message.entities[0].user.id).status not in stats:
                            app.kick_chat_member(message.chat.id, user_mention(message.text), 0)
                            message.edit('[{}](tg://user?id={}) is banned'.format(
                                message.entities[0].user.first_name, message.entities[0].user.id
                            ))
                            return
                        message.edit('Yout can\'t ban admin')
                        return
                    message.edit('You should use like this ".ban @username"')
                    return


@Client.on_message(filters.me & filters.command(['unban'], ['.', '/']))
def unban_user(app, message):
    chat_type = message.chat.type
    stats = ("creator", "administrator")
    if chat_type != "private":
        if app.get_chat_member(message.chat.id, app.get_me().id).status in stats:
            if message.reply_to_message:
                app.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                if message.reply_to_message.from_user.username:
                    message.edit(f'@{message.reply_to_message.from_user.username} is unbanned')
                    return
                message.edit('[{}](tg://user?id={}) is unbanned'.format(
                    message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id
                ), parse_mode="Markdown", disable_web_page_preview=True)
                return
        if message.entities:
            if message.entities[0].type == 'mention':
                if len(message.text.split()) == 2:
                    app.unban_chat_member(message.chat.id, user_mention(message.text))
                    message.edit(f'@{user_mention(message.text)} is unbanned')
                    return
                message.edit('You should use like this ".unban @username"')
                return
            if message.entities[0].type == 'text_mention':
                if len(message.text.split()) == 2:
                    app.unban_chat_member(message.chat.id, user_mention(message.text))
                    message.edit('[{}](tg://user?id={}) is unbanned'.format(
                        message.entities[0].user.first_name, message.entities[0].user.id
                    ))
                    return
                message.edit('You should use like this ".unban user_mention"')
                return


@Client.on_message(filters.me & filters.command(['gban'], ['.', '/']))
def gban_user(app, message):
    chat_type = message.chat.type
    stats = ("creator", "administrator")
    if chat_type != "private":
        if app.get_chat_member(message.chat.id, app.get_me().id).status in stats:
            if message.reply_to_message:
                if app.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status not in stats:
                    for i in app.iter_dialogs():
                        if i.chat.type != "private" and app.get_chat_member(i.chat.id, app.get_me().id).status in stats:
                            app.kick_chat_member(i.chat.id, message.reply_to_message.from_user.id, 0)
                    if message.reply_to_message.from_user.username:
                        message.edit(f'User @{message.reply_to_message.from_user.username} is gbanned')
                        return
                    message.edit('[{}](tg://user?id={}) is gbanned'.format(
                        message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id
                    ), parse_mode="Markdown", disable_web_page_preview=True)
                    return
                message.edit('You can\'t ban admin')
                return
            if message.entities:
                if message.entities[0].type == 'mention':
                    if len(message.text.split()) == 2:
                        if app.get_chat_member(message.chat.id, user_mention(message.text)).status not in stats \
                                if user_mention(message.text) in\
                                   [i.user.username for i in app.iter_chat_members(message.chat.id)] else True:
                            for i in app.iter_dialogs():
                                if i.chat.type != "private" and app.get_chat_member(i.chat.id,
                                                                                    app.get_me().id).status in stats:
                                    app.kick_chat_member(i.chat.id, user_mention(message.text), 0)
                            message.edit(f'@{user_mention(message.text)} is gbanned')
                            return
                    else:
                        message.edit('You should use like this ".gban @username"')
                        return
                elif message.entities[0].type == 'text_mention':
                    if len(message.text.split()) == 2:
                        if app.get_chat_member(message.chat.id, message.entities[0].user.id).status not in stats:
                            for i in app.iter_dialogs():
                                if i.chat.type != "private" and app.get_chat_member(i.chat.id,
                                                                                    app.get_me().id).status in stats:
                                    app.kick_chat_member(i.chat.id, user_mention(message.text), 0)
                            message.edit('[{}](tg://user?id={}) is gbanned'.format(
                                message.entities[0].user.first_name, message.entities[0].user.id
                            ))
                            return
                        message.edit('Yout can\'t ban admin')
                        return
                    message.edit('You should use like this ".gban @username"')
                    return


@Client.on_message(filters.me & filters.command(['ungban'], ['.', '/']))
def ungban_user(app, message):
    chat_type = message.chat.type
    stats = ("creator", "administrator")
    if chat_type != "private":
        if app.get_chat_member(message.chat.id, app.get_me().id).status in stats:
            if message.reply_to_message:
                for i in app.iter_dialogs():
                    if i.chat.tpye != "private" and app.get_chat_member(i.chat.id, app.get_me().id).status in stats:
                        app.unban_chat_member(i.chat.id, message.reply_to_message.from_user.id)
                if message.reply_to_message.from_user.username:
                    message.edit(f'@{message.reply_to_message.from_user.username} is ungbanned')
                    return
                message.edit('[{}](tg://user?id={}) is ungbanned'.format(
                    message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id
                ), parse_mode="Markdown", disable_web_page_preview=True)
                return
        if message.entities:
            if message.entities[0].type == 'mention':
                if len(message.text.split()) == 2:
                    for i in app.iter_dialogs():
                        if i.chat.type != "private" and app.get_chat_member(i.chat.id, app.get_me().id).status in stats:
                            app.unban_chat_member(i.chat.id, user_mention(message.text))
                    message.edit(f'@{user_mention(message.text)} is ungbanned')
                    return
                message.edit('You should use like this ".ungban @username"')
                return
            if message.entities[0].type == 'text_mention':
                if len(message.text.split()) == 2:
                    for i in app.iter_dialogs():
                        if i.chat.tpye != "private" and app.get_chat_member(i.chat.id, app.get_me().id).status in stats:
                            app.unban_chat_member(i.chat.id, user_mention(message.text))
                    message.edit('[{}](tg://user?id={}) is ungbanned'.format(
                        message.entities[0].user.first_name, message.entities[0].user.id
                    ))
                    return
                message.edit('You should use like this ".ungban user_mention"')
                return
