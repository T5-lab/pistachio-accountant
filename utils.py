from kivymd.uix.label import MDLabel
import os
from kivy.clock import Clock
from cryptography.fernet import Fernet
import json
from kivymd.toast import toast
from arabic_reshaper import reshape
import datetime


class Utils:
    def __init__(self, app):
        self.app = app
        self.key = b"e9_wA-2nAzR1dMlVJc0Fw6LcryeRHDPsxOLxs-Fz7-o="
        self.font = "IRAN Sans Bold.ttf"

    @staticmethod
    def err_lbl(**kwargs):
        if "pos_hint" not in kwargs:
            kwargs["pos_hint"] = {"center_x": 0.5, "center_y": 0.5}
        if "timeout" not in kwargs:
            kwargs["timeout"] = 4
        err_widget = MDLabel(text=kwargs["text"], pos_hint=kwargs["pos_hint"],
                             halign="center", theme_text_color="Custom",
                             text_color=kwargs["text_color"])
        kwargs["parent"].add_widget(err_widget)
        Clock.schedule_once(lambda x: kwargs["parent"].remove_widget(err_widget), kwargs["timeout"])

    def make_user_dirs(self, username):
        os.mkdir(self.app.database_dir + "\\" + username)
        os.mkdir(self.app.database_dir + "\\" + username + "\\" + "theme")
        os.mkdir(self.app.database_dir + "\\" + username + "\\" + "credentials")
        os.mkdir(self.app.database_dir + "\\" + username + "\\" + "persons")

    def create_dirs_obj(self, username):
        self.app.dirs["base_dir"] = self.app.database_dir + "\\" + username
        self.app.dirs["credentials"] = self.app.database_dir + "\\" + username + "\\" + "credentials"
        self.app.dirs["persons"] = self.app.database_dir + "\\" + username + "\\" + "persons"
        self.app.dirs["theme"] = self.app.database_dir + "\\" + username + "\\" + "theme"

    def encrypt_creds(self, username, password):
        creds = json.dumps({"username": username, "password": password})
        creds = Fernet(self.key).encrypt(creds.encode("utf-8"))
        return creds

    @staticmethod
    def save_creds(creds, path):
        with open(path, "wb") as f:
            f.write(creds)

    def change_password(self, dialog_instance, new_password):
        if not new_password:
            toast("Enter a valid password")
            return
        with open(self.app.dirs["credentials"] + "\\" + "creds.txt", "rb") as f:
            creds = self.decrypt_data(f.read())
            creds["password"] = new_password
            creds = self.encrypt_creds(creds["username"], creds["password"])
            self.save_creds(creds, self.app.dirs["credentials"] + "\\" + "creds.txt")
        toast("Password has been successfully changed")
        dialog_instance.dismiss()

    @staticmethod
    def show_password(text_field):
        if text_field.password:
            text_field.password = False
        else:
            text_field.password = True

    @staticmethod
    def reverse_text(text):
        return reshape(text)[::-1]

    def go_to_page(self, page):
        self.app.root.ids.nav_layout.ids.screen_manager.current = page

    def encrypt_data(self, data):
        return Fernet(self.key).encrypt(json.dumps(data).encode("utf-8"))

    def decrypt_data(self, data):
        return json.loads(Fernet(self.key).decrypt(data).decode("utf-8"))

    def save_kal_order(self, mode, obj):
        if not obj.ids.price.text or not obj.ids.weight.text or not obj.ids.value.text or not obj.ids.description.text \
                or obj.ids.person_label.text == self.reverse_text("موردی انتخاب نشده"):
            toast("Please enter all the fields.")
            return -1
        order_info = {"username": obj.ids.person_label.text,
                      "weight": obj.ids.weight.text,
                      "value": obj.ids.value.text,
                      "price": obj.ids.price.text,
                      "description": obj.ids.description.text}
        data = self.encrypt_data(order_info)
        self.save_creds(data, self.app.dirs["persons"] + "\\" + obj.ids.person_label.text + "\\" + "kal" + "\\"
                        + mode + "\\" + str(datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")) + ".txt")
        toast("order submitted")
        self.go_to_page("main_page")
        obj.ids.person_label.text = self.reverse_text("موردی انتخاب نشده")
        obj.ids.weight.text = obj.ids.value.text = obj.ids.price.text = obj.ids.description.text = ""

    def save_taze_khoshk_order(self, _type, mode, obj):
        if not obj.ids.type.text or not obj.ids.weight.text or not obj.ids.pure_weight.text or not obj.ids.value.text \
                or not obj.ids.total.text or obj.ids.person_label.text == self.reverse_text("موردی انتخاب نشده"):
            toast("Please enter all the fields")
            return -1
        order_info = {"username": obj.ids.person_label.text,
                      "type": obj.ids.type.text,
                      "weight": obj.ids.weight.text,
                      "pure_weight": obj.ids.pure_weight.text,
                      "value": obj.ids.value.text,
                      "total": obj.ids.total.text}
        data = self.encrypt_data(order_info)
        self.save_creds(data, self.app.dirs["persons"] + "\\" + obj.ids.person_label.text + "\\" + _type + "\\"
                        + mode + "\\" + str(datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")) + ".txt")
        toast("order submitted")
        self.go_to_page("main_page")
        obj.ids.person_label.text = self.reverse_text("موردی انتخاب نشده")
        obj.ids.weight.text = obj.ids.value.text = obj.ids.pure_weight.text = obj.ids.type.text = obj.ids.total.text = ""
