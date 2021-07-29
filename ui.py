ui = """
<PersianTextField@TextInput>:
    multiline: 0
    font_name: app.utils.font
    font_size: 15
    padding_y: [15,0]
    padding_x: [self.size[0]-self._get_text_width(max(self._lines, key=len), self.tab_width, self._label_cached)-10,8]

<ToolBar@BoxLayout>:
    orientation: "vertical"
    MDToolbar:
        title: "Khorami pistachio"
        left_action_items: [["menu", lambda x: app.root.ids.nav_layout.ids.nav_drawer.set_state("open")]]
        right_action_items: [["home", lambda x: app.utils.go_to_page("main_page")]]
    Widget:

<LoginPage@BoxLayout>:
    orientation: "vertical"
    padding: 200
    spacing: 30
    MDTextField:
        id: username
        hint_text: "Enter Username"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: None
        width: 300
    MDTextField:
        id: password
        hint_text: "Enter password"
        password: True
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: None
        width: 300
    MDRaisedButton:
        text: "Login"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        halign: "center"
        on_release: app.login(self.parent.ids.username.text, self.parent.ids.password.text)
    MDRaisedButton:
        text: "Create Account"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        halign: "center"
        on_release: app.root.current = "create_account"

<CreateAccountPage@BoxLayout>:
    orientation: "vertical"
    padding: 200
    spacing: 30
    MDIconButton:
        icon: "page-previous"
        halign: "left"
        on_release: app.root.current = "login"
    MDTextField:
        id: username
        hint_text: "Enter Username"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: None
        width: 300
        required: True
    MDTextField:
        id: password
        hint_text: "Enter password"
        password: True
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: None
        width: 300
        required: True
    MDRaisedButton:
        text: "Create"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        halign: "center"
        on_release: app.create_account(self.parent.ids.username.text, self.parent.ids.password.text)

<MainPage@FloatLayout>:
    MDRaisedButton:
        text: app.utils.reverse_text("خرید کال")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.3, "center_y": 0.8}
        on_release: app.utils.go_to_page("buy_kal")
    MDRaisedButton:
        text: app.utils.reverse_text("خرید تازه")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.3, "center_y": 0.6}
        on_release: app.utils.go_to_page("buy_taze")
    MDRaisedButton:
        text: app.utils.reverse_text("خرید خشک")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.3, "center_y": 0.4}
        on_release: app.utils.go_to_page("buy_khoshk")
    MDRaisedButton:
        text: app.utils.reverse_text("خرید متفرغه")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.3, "center_y": 0.2}
    MDRaisedButton:
        text: app.utils.reverse_text("فروش کال")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.7, "center_y": 0.8}
        on_release: app.utils.go_to_page("sell_kal")
    MDRaisedButton:
        text: app.utils.reverse_text("فروش تازه")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.7, "center_y": 0.6}
        on_release: app.utils.go_to_page("sell_taze")
    MDRaisedButton:
        text: app.utils.reverse_text("فروش خشک")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.7, "center_y": 0.4}
        on_release: app.utils.go_to_page("sell_khoshk")
    MDRaisedButton:
        text: app.utils.reverse_text("فروش متفرغه")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.7, "center_y": 0.2}
    MDIconButton:
        icon: "page-next"
        on_release: app.utils.go_to_page("second_page")
        pos_hint: {"center_x": 0.9, "center_y": 0.5}

<AddPersonPage@BoxLayout>:
    orientation: "vertical"
    padding: 150
    spacing: 50
    MDLabel:
        text: app.utils.reverse_text("نام و نام خانوادگی")
        font_name: app.utils.font
    PersianTextField:
        id: name
        hint_text: "name"
        size_hint_x: None
        width: 300
        size_hint_y: None
        height: 100
        font_name: app.utils.font
    MDRaisedButton:
        text: app.utils.reverse_text("تایید")
        font_name: app.utils.font
        on_release: app.add_person(self.parent.ids.name)
        
<ChoosePerson@ScrollView>:
    size_hint: [1, None]
    size: [Window.width, Window.height - dp(70)]

<BuyKalPage@FloatLayout>:
    MDLabel:
        text: app.utils.reverse_text("نام و نام خانوادگی")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.8}
    MDRaisedButton:
        text: app.utils.reverse_text("انتخاب")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.2, "center_y": 0.8}
        on_release: app.choose_person("buy_kal")
    MDLabel:
        id: person_label
        text: app.utils.reverse_text("موردی انتخاب نشده")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.9, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("وزن")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.65}
    MDTextField:
        id: weight
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.65}
    MDLabel:
        text: app.utils.reverse_text("فی")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.5}
    MDTextField:
        id: value
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.5}
    MDLabel:
        text: app.utils.reverse_text("مبلغ")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.35}
    MDTextField:
        id: price
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.35}
    MDLabel:
        text: app.utils.reverse_text("توضیحات")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.2}
    PersianTextField:
        id: description
        size_hint_y: None
        height: 150
        size_hint_x: None
        width: 400
        pos_hint: {"center_x": 0.3, "center_y": 0.15}
    MDRaisedButton:
        text: app.utils.reverse_text("ثبت")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.73, "center_y": 0.1}
        on_release: app.utils.save_kal_order("buys", self.parent)

<SellKalPage@FloatLayout>:
    MDLabel:
        text: app.utils.reverse_text("نام و نام خانوادگی")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.8}
    MDRaisedButton:
        text: app.utils.reverse_text("انتخاب")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.2, "center_y": 0.8}
        on_release: app.choose_person("sell_kal")
    MDLabel:
        id: person_label
        text: app.utils.reverse_text("موردی انتخاب نشده")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.9, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("وزن")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.65}
    MDTextField:
        id: weight
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.65}
    MDLabel:
        text: app.utils.reverse_text("فی")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.5}
    MDTextField:
        id: value
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.5}
    MDLabel:
        text: app.utils.reverse_text("مبلغ")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.35}
    MDTextField:
        id: price
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.35}
    MDLabel:
        text: app.utils.reverse_text("توضیحات")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.2}
    PersianTextField:
        id: description
        size_hint_y: None
        height: 150
        size_hint_x: None
        width: 400
        pos_hint: {"center_x": 0.3, "center_y": 0.15}
    MDRaisedButton:
        text: app.utils.reverse_text("ثبت")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.73, "center_y": 0.1}
        on_release: app.utils.save_kal_order("sells", self.parent)


<BuyTazePage@FloatLayout>:
    MDLabel:
        text: app.utils.reverse_text("نام و نام خانوادگی")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.8}
    MDRaisedButton:
        text: app.utils.reverse_text("انتخاب")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.2, "center_y": 0.8}
        on_release: app.choose_person("buy_taze")
    MDLabel:
        id: person_label
        text: app.utils.reverse_text("موردی انتخاب نشده")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.9, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("نوع پسته")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.7}
    PersianTextField:
        id: type
        size_hint_y: None
        height: 60
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.7}
    MDLabel:
        text: app.utils.reverse_text("وزن")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.6}
    MDTextField:
        id: weight
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.6}
    MDLabel:
        text: app.utils.reverse_text("وزن خالص")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.5}
    MDTextField:
        id: pure_weight
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.5}
    MDLabel:
        text: app.utils.reverse_text("فی")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.4}
    MDTextField:
        id: value
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.4}
    MDLabel:
        text: app.utils.reverse_text("جمع کل")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.3}
    MDTextField:
        id: total
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.3}
    MDRaisedButton:
        text: app.utils.reverse_text("ثبت")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.2, "center_y": 0.15}
        on_release: app.utils.save_taze_khoshk_order("taze", "buys", self.parent)


<SellTazePage@FloatLayout>:
    MDLabel:
        text: app.utils.reverse_text("نام و نام خانوادگی")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.8}
    MDRaisedButton:
        text: app.utils.reverse_text("انتخاب")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.2, "center_y": 0.8}
        on_release: app.choose_person("sell_taze")
    MDLabel:
        id: person_label
        text: app.utils.reverse_text("موردی انتخاب نشده")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.9, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("نوع پسته")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.7}
    PersianTextField:
        id: type
        size_hint_y: None
        height: 60
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.7}
    MDLabel:
        text: app.utils.reverse_text("وزن")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.6}
    MDTextField:
        id: weight
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.6}
    MDLabel:
        text: app.utils.reverse_text("وزن خالص")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.5}
    MDTextField:
        id: pure_weight
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.5}
    MDLabel:
        text: app.utils.reverse_text("فی")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.4}
    MDTextField:
        id: value
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.4}
    MDLabel:
        text: app.utils.reverse_text("جمع کل")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.3}
    MDTextField:
        id: total
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.3}
    MDRaisedButton:
        text: app.utils.reverse_text("ثبت")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.2, "center_y": 0.15}
        on_release: app.utils.save_taze_khoshk_order("taze", "sells", self.parent)


<BuyKhoshkPage@FloatLayout>:
    MDLabel:
        text: app.utils.reverse_text("نام و نام خانوادگی")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.8}
    MDRaisedButton:
        text: app.utils.reverse_text("انتخاب")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.2, "center_y": 0.8}
        on_release: app.choose_person("buy_khoshk")
    MDLabel:
        id: person_label
        text: app.utils.reverse_text("موردی انتخاب نشده")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.9, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("نوع پسته")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.7}
    PersianTextField:
        id: type
        size_hint_y: None
        height: 60
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.7}
    MDLabel:
        text: app.utils.reverse_text("وزن")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.6}
    MDTextField:
        id: weight
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.6}
    MDLabel:
        text: app.utils.reverse_text("وزن خالص")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.5}
    MDTextField:
        id: pure_weight
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.5}
    MDLabel:
        text: app.utils.reverse_text("فی")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.4}
    MDTextField:
        id: value
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.4}
    MDLabel:
        text: app.utils.reverse_text("جمع کل")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.3}
    MDTextField:
        id: total
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.3}
    MDRaisedButton:
        text: app.utils.reverse_text("ثبت")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.2, "center_y": 0.15}
        on_release: app.utils.save_taze_khoshk_order("khoshk", "buys", self.parent)

<SellKhoshkPage@FloatLayout>:
    MDLabel:
        text: app.utils.reverse_text("نام و نام خانوادگی")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.8}
    MDRaisedButton:
        text: app.utils.reverse_text("انتخاب")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.2, "center_y": 0.8}
        on_release: app.choose_person("sell_khoshk")
    MDLabel:
        id: person_label
        text: app.utils.reverse_text("موردی انتخاب نشده")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.9, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("نوع پسته")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.7}
    PersianTextField:
        id: type
        size_hint_y: None
        height: 60
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.7}
    MDLabel:
        text: app.utils.reverse_text("وزن")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.6}
    MDTextField:
        id: weight
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.6}
    MDLabel:
        text: app.utils.reverse_text("وزن خالص")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.5}
    MDTextField:
        id: pure_weight
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.5}
    MDLabel:
        text: app.utils.reverse_text("فی")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.4}
    MDTextField:
        id: value
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.4}
    MDLabel:
        text: app.utils.reverse_text("جمع کل")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.2, "center_y": 0.3}
    MDTextField:
        id: total
        size_hint_x: None
        width: 200
        pos_hint: {"center_x": 0.2, "center_y": 0.3}
    MDRaisedButton:
        text: app.utils.reverse_text("ثبت")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.2, "center_y": 0.15}
        on_release: app.utils.save_taze_khoshk_order("khoshk", "sells", self.parent)

<KalFactors@FloatLayout>:
    MDLabel:
        text: app.utils.reverse_text("نام و نام خانوادگی")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.57, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("وزن")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.8, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("فی")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.0, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("مبلغ")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.18, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("توضیحات")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.37, "center_y": 0.8}
    ScrollView:
        size_hint: [1, None]
        size: [Window.width, Window.height - dp(180)]
        id: scroll_view

<TazeKhoshkFactors@FloatLayout>:
    MDLabel:
        text: app.utils.reverse_text("نام و نام خانوادگی")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.55, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("نوع پسته")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.73, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("وزن")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.9, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("وزن خالص")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.045, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("فی")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.23, "center_y": 0.8}
    MDLabel:
        text: app.utils.reverse_text("جمع کل")
        font_name: app.utils.font
        pos_hint: {"center_x": 1.36, "center_y": 0.8}
    ScrollView:
        size_hint: [1, None]
        size: [Window.width, Window.height - dp(180)]
        id: scroll_view

<SecondPage@FloatLayout>:
    MDRaisedButton:
        text: app.utils.reverse_text("فاکتور خرید کال")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.3, "center_y": 0.8}
        on_release: app.make_kal_factors("buys")
    MDRaisedButton:
        text: app.utils.reverse_text("فاکتور خرید تازه")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.3, "center_y": 0.6}
        on_release: app.make_taze_khoshk_factors("taze", "buys")
    MDRaisedButton:
        text: app.utils.reverse_text("فاکتور خرید خشک")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.3, "center_y": 0.4}
        on_release: app.make_taze_khoshk_factors("khoshk", "buys")
    MDRaisedButton:
        text: app.utils.reverse_text("فاکتور خرید متفرغه")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.3, "center_y": 0.2}
    MDRaisedButton:
        text: app.utils.reverse_text("فاکتور فروش کال")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.7, "center_y": 0.8}
        on_release: app.make_kal_factors("sells")
    MDRaisedButton:
        text: app.utils.reverse_text("فاکتور فروش تازه")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.7, "center_y": 0.6}
        on_release: app.make_taze_khoshk_factors("taze", "sells")
    MDRaisedButton:
        text: app.utils.reverse_text("فاکتور فروش خشک")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.7, "center_y": 0.4}
        on_release: app.make_taze_khoshk_factors("khoshk", "sells")
    MDRaisedButton:
        text: app.utils.reverse_text("فاکتور فروش متفرغه")
        font_name: app.utils.font
        pos_hint: {"center_x": 0.7, "center_y": 0.2}

<NavLayout@MDNavigationLayout>:
    ScreenManager:
        Screen:
            ToolBar:
            ScreenManager:
                id: screen_manager
                Screen:
                    name: "main_page"
                    MainPage:
                Screen:
                    name: "second_page"
                    SecondPage:
                Screen:
                    name: "add_person"
                    AddPersonPage:
                        id: add_person
                Screen:
                    name: "buy_kal"
                    BuyKalPage:
                        id: buy_kal
                Screen:
                    name: "sell_kal"
                    SellKalPage:
                        id: sell_kal
                Screen:
                    name: "buy_taze"
                    BuyTazePage:
                        id: buy_taze
                Screen:
                    name: "sell_taze"
                    SellTazePage:
                        id: sell_taze
                Screen:
                    name: "buy_khoshk"
                    BuyKhoshkPage:
                        id: buy_khoshk
                Screen:
                    name: "sell_khoshk"
                    SellKhoshkPage:
                        id: sell_khoshk
                Screen:
                    name: "choose_person"
                    ChoosePerson:
                        id: choose_person
                Screen:
                    name: "kal_factors"
                    KalFactors:
                        id: kal_factors
                Screen:
                    name: "taze_khoshk_factors"
                    TazeKhoshkFactors:
                        id: taze_khoshk_factors
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: "vertical"
            MDLabel:
                size_hint: [1, 0.3]
                id: welcome_lbl
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                halign: "center"
            ScrollView:
                MDList:
                    OneLineAvatarListItem:
                        text: "Add a person"
                        on_release: app.utils.go_to_page("add_person")
                        ImageLeftWidget:
                            source: "add-person.png"
                    OneLineIconListItem:
                        text: "Theme"
                        on_release: app.show_theme_picker()
                        IconLeftWidget:
                            icon: "theme-light-dark"
                            on_release: app.show_theme_picker()
                    OneLineIconListItem:
                        text: "Change Password"
                        on_release: app.change_password()
                        IconLeftWidget:
                            icon: "key-change"
                            on_release: app.change_password()
                    OneLineIconListItem:
                        text: "Logout"
                        on_release: app.root.current = "login"
                        IconLeftWidget:
                            icon: "logout"
                            on_release: app.logout()
                        
ScreenManager:
    id: main_sm
    Screen:
        name: "login"
        LoginPage:
            id: login_page
    Screen:
        name: "create_account"
        CreateAccountPage:
            id: create_account_page
    Screen:
        name: "app"
        NavLayout:
            id: nav_layout
"""