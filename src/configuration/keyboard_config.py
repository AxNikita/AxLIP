from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class KeyboardConfiguration:
    def __init__(self):
        self.keyboard_button = [
            [
                KeyboardButton(text="📖"),
                KeyboardButton(text="📚")
            ]
        ]
        self.keyboard = ReplyKeyboardMarkup(
            keyboard=self.keyboard_button,
            resize_keyboard=True,
            input_field_placeholder="Введите вашу страницу"
        )

    def get_keyboard_button(self):
        return self.keyboard_button

    def get_keyboard(self):
        return self.keyboard
