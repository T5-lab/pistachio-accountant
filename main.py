from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.picker import MDThemePicker
import os
from utils import Utils
from ui import ui
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton
import arabic_reshaper
from bidi.algorithm import get_display
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel
from kivymd.toast import toast
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.widget import Widget


class PersianTextField(TextInput):
    max_chars = NumericProperty(80)  # maximum character allowed
    str = StringProperty()

    def __init__(self, **kwargs):
        super(PersianTextField, self).__init__(**kwargs)
        self.text = get_display(arabic_reshaper.reshape(" "))

    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.text) + len(substring) > self.max_chars):
            return
        self.str = self.str + substring
        self.text = get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(PersianTextField, self).insert_text(substring, from_undo)

    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str) - 1]
        self.text = get_display(arabic_reshaper.reshape(self.str))


class MainApp(MDApp):
    def __init__(self):
        super(MainApp, self).__init__()
        self.database_dir = os.path.expanduser("~") + "\\" + "Hesabdari"
        self.utils = Utils(self)
        self.title = "Khorami pistachio"
        self.user = None
        self.dirs = {}
        self.buttons = {}
        self.table_row_labels = {0: [], 1: []}
        Window.on_resize = self.on_resize

    def build(self):
        return Builder.load_string(ui)

    def login(self, username, password):
        if username and password:
            try:
                with open(self.database_dir + "\\" + username + "\\" + "credentials" + "\\"
                          + "creds.txt", "rb") as f:
                    creds = self.utils.decrypt_data(f.read())
                    if creds["password"] == password:
                        self.user = username
                        self.utils.create_dirs_obj(username)
                        self.root.ids.nav_layout.ids.welcome_lbl.text = f"Welcome {self.user}"
                        self.apply_user_theme()
                        self.root.current = "app"
                    else:
                        toast("Invalid password")
            except:
                toast("Invalid Username")
        else:
            toast("Make sure you filled all the fields")

    def create_account(self, username, password):
        if username and password:
            try:
                self.utils.make_user_dirs(username)
                self.utils.create_dirs_obj(username)
                creds = self.utils.encrypt_creds(username, password)
                self.utils.save_creds(creds, self.database_dir + "\\" + username + "\\" + "credentials" + "\\"
                                      + "creds.txt")
                self.root.current = "app"
                self.user = username
                self.root.ids.nav_layout.ids.welcome_lbl.text = f"Welcome {self.user}"
            except:
                toast("Invalid Username")
        else:
            toast("Make sure you filled all the fields")

    def change_password(self):
        new_password = MDTextField(pos_hint={"center_x": 0.5, "center_y": 0.5}, size_hint_x=None, width=300)
        new_password.hint_text = "Enter new password"
        new_password.password = True
        show_btn = MDIconButton(icon='eye', on_release=lambda x: self.utils.show_password(new_password))
        cancel_btn = MDFlatButton(text="Cancel", on_release=lambda x: dialog.dismiss())
        confirm_btn = MDFlatButton(text="Confirm",
                                   on_release=lambda x: self.utils.change_password(dialog, new_password.text))
        dialog = MDDialog(title="Change password", pos_hint={"center_x": 0.5, "center_y": 0.5},
                          buttons=[cancel_btn, confirm_btn])
        layout = BoxLayout(padding=20, size_hint=[None, None], width=300, height=100)
        layout.add_widget(new_password)
        layout.add_widget(show_btn)
        dialog.add_widget(layout)
        dialog.open()

    @staticmethod
    def show_theme_picker():
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def add_person(self, name):
        try:
            os.mkdir(self.dirs["persons"] + "\\" + name.text)
            os.mkdir(self.dirs["persons"] + "\\" + name.text + "\\" + "kal")
            os.mkdir(self.dirs["persons"] + "\\" + name.text + "\\" + "kal" + "\\" + "buys")
            os.mkdir(self.dirs["persons"] + "\\" + name.text + "\\" + "kal" + "\\" + "sells")
            os.mkdir(self.dirs["persons"] + "\\" + name.text + "\\" + "taze")
            os.mkdir(self.dirs["persons"] + "\\" + name.text + "\\" + "taze" + "\\" + "buys")
            os.mkdir(self.dirs["persons"] + "\\" + name.text + "\\" + "taze" + "\\" + "sells")
            os.mkdir(self.dirs["persons"] + "\\" + name.text + "\\" + "khoshk")
            os.mkdir(self.dirs["persons"] + "\\" + name.text + "\\" + "khoshk" + "\\" + "buys")
            os.mkdir(self.dirs["persons"] + "\\" + name.text + "\\" + "khoshk" + "\\" + "sells")
            os.mkdir(self.dirs["persons"] + "\\" + name.text + "\\" + "motefareqe")
            os.mkdir(self.dirs["persons"] + "\\" + name.text + "\\" + "motefareqe" + "\\" + "buys")
            os.mkdir(self.dirs["persons"] + "\\" + name.text + "\\" + "motefareqe" + "\\" + "sells")
            toast("Person has been added successfully")
            name.text = ""
            self.utils.go_to_page("main_page")
        except Exception as e:
            toast("This person already exists")
            print(e)

    def choose_person(self, mode):
        self.root.ids.nav_layout.ids.choose_person.clear_widgets()
        layout = GridLayout(cols=2, spacing=30, size_hint_y=None)
        layout.bind(minimum_height=layout.setter("height"))
        for idx, person in enumerate(os.listdir(self.dirs["persons"])):
            label = MDLabel(text=person, size_hint_y=None, height=40)
            label.font_name = self.utils.font
            layout.add_widget(label)
            self.buttons[idx] = MDRaisedButton(text=self.utils.reverse_text("انتخاب"), size_hint_y=None, height=40,
                                               font_name=self.utils.font,
                                               on_release=lambda x: self.save_person(x, mode))
            layout.add_widget(self.buttons[idx])
        self.root.ids.nav_layout.ids.choose_person.add_widget(layout)
        self.utils.go_to_page("choose_person")

    def save_person(self, obj, mode):
        persons = os.listdir(self.dirs["persons"])
        for key in self.buttons.keys():
            if obj == self.buttons[key]:
                if mode == "buy_kal":
                    self.root.ids.nav_layout.ids.buy_kal.ids.person_label.text = persons[key]
                elif mode == "sell_kal":
                    self.root.ids.nav_layout.ids.sell_kal.ids.person_label.text = persons[key]
                elif mode == "buy_taze":
                    self.root.ids.nav_layout.ids.buy_taze.ids.person_label.text = persons[key]
                elif mode == "sell_taze":
                    self.root.ids.nav_layout.ids.sell_taze.ids.person_label.text = persons[key]
                elif mode == "buy_khoshk":
                    self.root.ids.nav_layout.ids.buy_khoshk.ids.person_label.text = persons[key]
                elif mode == "sell_khoshk":
                    self.root.ids.nav_layout.ids.sell_khoshk.ids.person_label.text = persons[key]
                self.utils.go_to_page(mode)
                break

    def make_kal_factors(self, mode):
        scroll_view = self.root.ids.nav_layout.ids.kal_factors.ids.scroll_view
        scroll_view.clear_widgets()
        self.table_row_labels[0].clear()
        layout = GridLayout(cols=6, spacing=30, size_hint_y=None)
        layout.bind(minimum_height=layout.setter("height"))
        for person in os.listdir(self.dirs["persons"]):
            for factor in os.listdir(self.dirs["persons"] + "\\" + person + "\\" + "kal" + "\\" + mode):
                with open(os.path.join(self.dirs["persons"] + "\\" + person + "\\" + "kal" + "\\" + mode + "\\"
                                       + factor), "rb") as f:
                    data = self.utils.decrypt_data(f.read())
                layout.add_widget(Widget(size_hint_x=None, width=15))
                for i in data:
                    label = MDLabel(text=data[i], size_hint_x=None, width=dp((Window.width / 5) - 40), size_hint_y=None,
                                    height=dp(40), md_bg_color=self.theme_cls.accent_color, halign="center")
                    label.font_name = self.utils.font
                    self.table_row_labels[0].append(label)
                    layout.add_widget(label)
        scroll_view.add_widget(layout)
        self.utils.go_to_page("kal_factors")

    def make_taze_khoshk_factors(self, _type, mode):
        scroll_view = self.root.ids.nav_layout.ids.taze_khoshk_factors.ids.scroll_view
        scroll_view.clear_widgets()
        self.table_row_labels[1].clear()
        layout = GridLayout(cols=7, spacing=30, size_hint_y=None)
        layout.bind(minimum_height=layout.setter("height"))
        for person in os.listdir(self.dirs["persons"]):
            for factor in os.listdir(self.dirs["persons"] + "\\" + person + "\\" + _type + "\\" + mode):
                with open(
                        os.path.join(self.dirs["persons"] + "\\" + person + "\\" + _type + "\\" + mode + "\\" + factor),
                        "rb") as f:
                    data = self.utils.decrypt_data(f.read())
                layout.add_widget(Widget(size_hint_x=None, width=15))
                for i in data:
                    label = MDLabel(text=data[i], size_hint_x=None, width=dp((Window.width/6) - 40), size_hint_y=None, height=dp(45),
                                    md_bg_color=self.theme_cls.accent_color, halign="center")
                    label.font_name = self.utils.font
                    self.table_row_labels[1].append(label)
                    layout.add_widget(label)
        scroll_view.add_widget(layout)
        self.utils.go_to_page("taze_khoshk_factors")

    def logout(self):
        self.user = None
        self.dirs = {}
        self.root.current = "login"

    def apply_user_theme(self):
        if os.path.isfile(self.dirs["theme"] + "\\" + "theme.txt"):
            with open(self.dirs["theme"] + "\\" + "theme.txt", "rb") as f:
                theme_data = self.utils.decrypt_data(f.read())
            self.theme_cls.primary_palette = theme_data["primary"]
            self.theme_cls.accent_palette = theme_data["accent"]
            self.theme_cls.theme_style = theme_data["theme_style"]

    def on_resize(self, *args):
        for label in self.table_row_labels[0]:
            label.width = dp((Window.width / 5) - 40)
        for label in self.table_row_labels[1]:
            label.width = dp((Window.width / 6) - 40)

    def on_start(self):
        if not os.path.isdir(self.database_dir):
            os.mkdir(self.database_dir)

    def on_stop(self):
        if self.user:
            theme_data = self.utils.encrypt_data(
                {"primary": self.theme_cls.primary_palette, "accent": self.theme_cls.accent_palette,
                 "theme_style": self.theme_cls.theme_style})
            with open(self.dirs["theme"] + "\\" + "theme.txt", "wb") as f:
                f.write(theme_data)


if __name__ == '__main__':
    MainApp().run()
