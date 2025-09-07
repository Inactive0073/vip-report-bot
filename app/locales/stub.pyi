from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    to: To
    a: A
    main: Main
    customer: Customer
    waiter: Waiter
    start: Start
    cr: Cr
    channel: Channel
    content: Content
    settings: Settings
    admin: Admin

    @staticmethod
    def next() -> Literal["""⏭ Далее"""]: ...

    @staticmethod
    def cancel() -> Literal["""❌Отмена"""]: ...

    @staticmethod
    def back() -> Literal["""🔙 Назад"""]: ...

    @staticmethod
    def error() -> Literal["""⚠ Произошла ошибка"""]: ...

    @staticmethod
    def yes() -> Literal["""✔ Да"""]: ...

    @staticmethod
    def no() -> Literal["""Нет"""]: ...

    @staticmethod
    def edit() -> Literal["""✍ Изменить"""]: ...

    @staticmethod
    def delete() -> Literal["""🧹 Удалить"""]: ...

    @staticmethod
    def add() -> Literal["""➕ Добавить"""]: ...

    @staticmethod
    def caption() -> Literal["""Сделано через &lt;a href=&#34;https://t.me/inactive0073&#34;&gt;&lt;b&gt;💵Sale Keeper&lt;/b&gt;&lt;/a&gt;"""]: ...


class To:
    @staticmethod
    def cancel() -> Literal["""✋ Отменить"""]: ...


class A:
    u: AU


class AU:
    @staticmethod
    def sure() -> Literal["""Вы уверены?"""]: ...


class Main:
    @staticmethod
    def menu() -> Literal["""Главное меню"""]: ...


class Customer:
    hello: CustomerHello
    meeting: CustomerMeeting
    error: CustomerError
    menu: CustomerMenu
    balance: CustomerBalance
    no: CustomerNo
    catalog: CustomerCatalog
    delivery: CustomerDelivery
    loyalty: CustomerLoyalty
    partnership: CustomerPartnership
    about: CustomerAbout
    support: CustomerSupport


class CustomerHello:
    @staticmethod
    def message() -> Literal["""Добро пожаловать в чат‑бот программы лояльности Surf Coffee x SUNDAY! 😊

Чтобы начать, отправьте, пожалуйста, Ваш номер телефона. Просто нажмите кнопку «Отправить контакт».👇

Поделившись номером, вы соглашаетесь с Политикой конфиденциальности и условиями программы лояльности, а также принимаете и соглашаетесь на обработку персональных данных. 👉&lt;a href=&#34;https://www.surfcoffee.ru/loyalty&#34;&gt;Здесь всё подробно&lt;/a&gt;:"""]: ...


class CustomerMeeting:
    gender: CustomerMeetingGender

    @staticmethod
    def phone() -> Literal["""Отправить контакт"""]: ...

    @staticmethod
    def name() -> Literal["""Отлично! Теперь, пожалуйста, представьтесь — как вас зовут?"""]: ...

    @staticmethod
    def surname() -> Literal["""Прекрасно! А теперь, пожалуйста, укажите вашу фамилию"""]: ...

    @staticmethod
    def email() -> Literal["""И ещё: ваш e‑mail 💌
Мы пришлём вам новости об акциях, свежих спотах и сезонных предложениях."""]: ...

    @staticmethod
    def birthday() -> Literal["""Укажите дату рождения в формате дд.мм.гггг — и получите подарок от нас! 🎁"""]: ...

    @staticmethod
    def thanks() -> Literal["""Отлично, спасибо! Добро пожаловать в сообщество Surf Coffee ❤️"""]: ...


class CustomerError:
    @staticmethod
    def phone() -> Literal["""Этот номер не совпадает с тем, с которого вы регистрировали аккаунт в телеграм. Нажмите &lt;b&gt;Отправить контакт&lt;/b&gt;"""]: ...

    @staticmethod
    def name() -> Literal["""Пожалуйста, введите ваше имя"""]: ...

    @staticmethod
    def surname() -> Literal["""Не получилось распознать. Введите фамилию снова"""]: ...

    @staticmethod
    def birthday() -> Literal["""Не распознали дату. Введите в формате &lt;b&gt;дд.мм.гггг&lt;/b&gt;"""]: ...


class CustomerMeetingGender:
    @staticmethod
    def __call__() -> Literal["""Почти готово! Укажите ваш пол:"""]: ...

    @staticmethod
    def m() -> Literal["""Мужской"""]: ...

    @staticmethod
    def f() -> Literal["""Женский"""]: ...


class CustomerMenu:
    info: CustomerMenuInfo
    balance: CustomerMenuBalance
    about: CustomerMenuAbout
    card: CustomerMenuCard
    gifts: CustomerMenuGifts
    delivery: CustomerMenuDelivery
    loyalty: CustomerMenuLoyalty
    partnership: CustomerMenuPartnership
    help: CustomerMenuHelp

    @staticmethod
    def placeholder() -> Literal["""Выберите пункт меню"""]: ...


class CustomerMenuInfo:
    @staticmethod
    def message() -> Literal["""Выберите интересующий раздел в меню — ясно и просто, жмите на значок 🎛 внизу экрана."""]: ...


class CustomerMenuBalance:
    @staticmethod
    def button() -> Literal["""Баланс и уровень"""]: ...


class CustomerMenuAbout:
    @staticmethod
    def button() -> Literal["""Наши кофейни ☕"""]: ...


class CustomerMenuCard:
    @staticmethod
    def button() -> Literal["""Показать карту"""]: ...


class CustomerMenuGifts:
    @staticmethod
    def button() -> Literal["""Подарки и бонусы"""]: ...


class CustomerMenuDelivery:
    @staticmethod
    def button() -> Literal["""Заказ и самовывоз"""]: ...


class CustomerMenuLoyalty:
    @staticmethod
    def button() -> Literal["""Условия программы"""]: ...


class CustomerMenuPartnership:
    @staticmethod
    def button() -> Literal["""Партнёрство"""]: ...


class CustomerMenuHelp:
    @staticmethod
    def button() -> Literal["""Помощь"""]: ...


class CustomerBalance:
    @staticmethod
    def message(*, current_balance, date_expire, balance_to_expire, visits, percent_cashback) -> Literal["""&lt;b&gt;Баланс и уровень&lt;/b&gt;

&lt;b&gt;Бонусных баллов:&lt;/b&gt; { $current_balance }
&lt;b&gt;Ближайшая дата сгорания:&lt;/b&gt; { $date_expire }
&lt;b&gt;Баллов к сгоранию:&lt;/b&gt; { $balance_to_expire }
&lt;b&gt;Посещений:&lt;/b&gt; { $visits }
&lt;b&gt;Кэшбэк:&lt;/b&gt; { $percent_cashback }%

Если вам недоступны бонусы и карта, поделитесь с нами своим номером телефона, вызвав команду /start"""]: ...


class CustomerNo:
    balance: CustomerNoBalance


class CustomerNoBalance:
    @staticmethod
    def message() -> Literal["""У вас пока нет баллов. Начните копить — приходи в спот!"""]: ...


class CustomerCatalog:
    @staticmethod
    def message() -> Literal["""Чтобы использовать баллы или получить подарок:

— Зайди в ближайший спот Surf Coffee назови номер своего телефона который привязан к программе лояльности;
— Продиктуй код баристе или менеджеру;
— Получай подарок за баллы 😉

Обратите внимание: сертификаты, приобретённые за баллы, не меняются и не возвращаются. Можете бронировать заранее!"""]: ...

    @staticmethod
    def button() -> Literal["""Показать карту спота"""]: ...

    @staticmethod
    def link() -> Literal["""https://www.surfcoffee.ru/surf-coffee-stores"""]: ...


class CustomerDelivery:
    @staticmethod
    def message() -> Literal["""У нас есть самовывоз и доставка. Учтите: программа лояльности действует только при посещении спота."""]: ...

    @staticmethod
    def button() -> Literal["""Заказать кофе"""]: ...

    @staticmethod
    def link() -> Literal["""https://www.surfcoffee.ru/"""]: ...


class CustomerLoyalty:
    @staticmethod
    def message() -> Literal["""Добро пожаловать в программу лояльности Surf Coffee x SUNDAY 😎

Что даёт вам участие?

- Кэшбэк 3–10% с каждого посещения
- Персональные акции и предложения — не пропустите в уведомлениях
- Доступ к каталогу подарков сразу после регистрации

Важно:
- Баллы начисляются с каждого чека
- Чтобы удержать уровень 10%, нужно совершить 20 визитов в течение года"""]: ...

    @staticmethod
    def button() -> Literal["""Условия программы"""]: ...

    @staticmethod
    def link() -> Literal["""https://www.surfcoffee.ru/loyalty"""]: ...


class CustomerPartnership:
    info: CustomerPartnershipInfo


class CustomerPartnershipInfo:
    @staticmethod
    def message() -> Literal["""Хотите стать партнёром? Пишите нам: &lt;a href=&#34;mailto:partnership@surfcoffee.ru&#34;&gt;partnership@surfcoffee.ru&lt;/a&gt;"""]: ...


class CustomerAbout:
    info: CustomerAboutInfo
    message: CustomerAboutMessage
    link: CustomerAboutLink


class CustomerAboutInfo:
    @staticmethod
    def message() -> Literal["""Surf Coffee x SUNDAY — уютный спот в духе мини‑лофта с панорамным светом, живыми растениями и круассанами, как в Париже."""]: ...


class CustomerAboutMessage:
    @staticmethod
    def menu() -> Literal["""Посмотреть меню"""]: ...

    @staticmethod
    def take() -> Literal["""Забронировать стол"""]: ...

    @staticmethod
    def delivery() -> Literal["""Самовывоз и доставка"""]: ...

    @staticmethod
    def schedule() -> Literal["""Режим работы"""]: ...

    @staticmethod
    def route() -> Literal["""Как добраться"""]: ...

    @staticmethod
    def social() -> Literal["""Мы в соцсетях"""]: ...


class CustomerAboutLink:
    @staticmethod
    def menu() -> Literal["""https://www.surfcoffee.ru/sunday#menu"""]: ...

    @staticmethod
    def take() -> Literal["""https://www.surfcoffee.ru/sunday#booking"""]: ...

    @staticmethod
    def delivery() -> Literal["""https://www.surfcoffee.ru/sunday#delivery"""]: ...

    @staticmethod
    def schedule() -> Literal["""https://www.surfcoffee.ru/sunday#hours"""]: ...

    @staticmethod
    def route() -> Literal["""https://www.surfcoffee.ru/sunday#location"""]: ...

    @staticmethod
    def social() -> Literal["""https://www.instagram.com/surfcoffee/"""]: ...


class CustomerSupport:
    @staticmethod
    def message() -> Literal["""Если нужна помощь — пишите нам через &lt;a href=&#34;https://www.surfcoffee.ru/contacts&#34;&gt;контакты&lt;/a&gt;."""]: ...


class Waiter:
    hello: WaiterHello
    pagination: WaiterPagination
    instruction: WaiterInstruction
    success: WaiterSuccess
    invalid: WaiterInvalid
    repeat: WaiterRepeat
    approve: WaiterApprove
    to: WaiterTo
    processing: WaiterProcessing


class WaiterHello:
    @staticmethod
    def message() -> Literal["""Ваша роль: &lt;b&gt;Официант&lt;/b&gt;
Для получения инструкции по работе с ботом, нажмите &lt;a href=&#34;/instruction&#34;&gt;/instruction&lt;/a&gt;"""]: ...


class WaiterPagination:
    @staticmethod
    def message(*, current_page, pages) -> Literal["""Страница { $current_page } из { $pages }."""]: ...


class WaiterInstruction:
    message: WaiterInstructionMessage


class WaiterInstructionMessage:
    @staticmethod
    def 1() -> Literal["""Напишите номер телефона абонента без специальных символов, только цифры."""]: ...

    @staticmethod
    def 2() -> Literal["""Вы получите базовую информацию о пользователе и его балансе."""]: ...

    @staticmethod
    def 3() -> Literal["""При попытке начисления баллов просто укажите итоговую сумму чека гостя. Рассчеты и запись в журнал произойдет автоматически."""]: ...

    @staticmethod
    def 4() -> Literal["""При попытке списания гостю поступит сообщение с кодом, которое вы должны ввести на своем устройстве и отправить его боту. 

&lt;i&gt;Если сообщение не поступает, убедитесь, что пользователь зарегистрирован в системе и он не заблокировал бота (&lt;b&gt;если бот был заблокирован гостем, то он не получит код&lt;/b&gt;)&lt;/i&gt;."""]: ...

    @staticmethod
    def 5() -> Literal["""В ответ вы получите информацию по пользователю, а также доступ к окну работы с клиентом."""]: ...

    @staticmethod
    def 6() -> Literal["""Далее необходимо ввести итоговую сумму чека клиента. Все необходимые рассчеты будут произведены автоматически. 

Просто проверьте, что чек верный и отправьте его боту. Готово ✅!"""]: ...

    @staticmethod
    def 7() -> Literal["""Инструкция 7"""]: ...

    @staticmethod
    def 8() -> Literal["""Инструкция 8"""]: ...

    @staticmethod
    def 9() -> Literal["""Инструкция 9"""]: ...

    @staticmethod
    def 10() -> Literal["""Инструкция 10"""]: ...


class WaiterSuccess:
    info: WaiterSuccessInfo


class WaiterSuccessInfo:
    @staticmethod
    def customer(*, name, balance, date_expire, bonus_to_expire) -> Literal["""Данные по пользователю успешно получены. 
---  
👤 &lt;b&gt;Имя:&lt;/b&gt; { $name }  
💰 &lt;b&gt;Кол-во бонусов:&lt;/b&gt; { $balance }  
📅 &lt;b&gt;Бонусы сгорают:&lt;/b&gt; { $date_expire }  
🔥 &lt;b&gt;Количество бонусов к списанию:&lt;/b&gt; { $bonus_to_expire }  
---"""]: ...


class WaiterInvalid:
    info: WaiterInvalidInfo
    code: WaiterInvalidCode


class WaiterInvalidInfo:
    @staticmethod
    def customer() -> Literal["""Нет данных по пользователю. Проверьте правильность номера телефона."""]: ...


class WaiterRepeat:
    code: WaiterRepeatCode


class WaiterRepeatCode:
    @staticmethod
    def msg() -> Literal["""Отправить код еще раз."""]: ...


class WaiterApprove:
    subtract: WaiterApproveSubtract


class WaiterApproveSubtract:
    @staticmethod
    def msg() -> Literal["""Введите код, отправленный клиенту."""]: ...


class WaiterTo:
    client: WaiterToClient


class WaiterToClient:
    @staticmethod
    def msg(*, code) -> Literal["""Ваш код: &lt;b&gt;&lt;i&gt;{ $code }&lt;/i&gt;&lt;/b&gt;"""]: ...


class WaiterInvalidCode:
    @staticmethod
    def msg() -> Literal["""Неверный код, проверьте правильность и попробуйте еще раз."""]: ...


class WaiterProcessing:
    add: WaiterProcessingAdd
    subtract: WaiterProcessingSubtract
    adding: WaiterProcessingAdding
    subtracting: WaiterProcessingSubtracting

    @staticmethod
    def instruction() -> Literal["""&lt;b&gt;РАБОТА С КЛИЕНТОМ&lt;/b&gt;

Для начисления: &lt;b&gt;➕Начисить бонусы&lt;/b&gt;
Для списания: &lt;b&gt;➖Списать бонусы&lt;/b&gt;
Для возврата: &lt;b&gt;🔙 Назад&lt;/b&gt;"""]: ...


class WaiterProcessingAdd:
    @staticmethod
    def bonus() -> Literal["""➕Начислить бонусы"""]: ...


class WaiterProcessingSubtract:
    @staticmethod
    def bonus() -> Literal["""➖Списать бонусы"""]: ...


class WaiterProcessingAdding:
    bonus: WaiterProcessingAddingBonus

    @staticmethod
    def success(*, amount) -> Literal["""Бонусы успешно начислены. 

&lt;b&gt;&lt;i&gt;Было начислено { $amount } б.&lt;/i&gt;&lt;/b&gt;"""]: ...

    @staticmethod
    def unsuccess() -> Literal["""Не удалось начислить бонусы. Проверьте данные и попробуйте снова."""]: ...


class WaiterProcessingAddingBonus:
    @staticmethod
    def instruction() -> Literal["""Введите сумму чека стола для начисления бонусов. 

Вводите именно итоговую сумму чека. Бонусы будут рассчитаны автоматически."""]: ...


class WaiterProcessingSubtracting:
    not_: WaiterProcessingSubtractingNot_

    @staticmethod
    def instruction() -> Literal["""Укажите сумму бонусов для списания."""]: ...

    @staticmethod
    def success() -> Literal["""Бонусы успешно списаны."""]: ...

    @staticmethod
    def unsuccess() -> Literal["""Не удалось списать бонусы. Проверьте данные и попробуйте снова. 

Возможно, вы указали неверную сумму или у вас недостаточно бонусов. Для возврата в основное меню нажмите &lt;a href=&#34;/reset&#34;&gt;/reset&lt;/a&gt;"""]: ...


class WaiterProcessingSubtractingNot_:
    @staticmethod
    def enough() -> Literal["""Введеное значение превышает доступное количество бонусов."""]: ...


class Start:
    hello: StartHello
    create: StartCreate
    my: StartMy
    add: StartAdd

    @staticmethod
    def settings() -> Literal["""Настройки"""]: ...


class StartHello:
    @staticmethod
    def admin() -> Literal["""Ваша роль: &lt;b&gt;Менеджер&lt;/b&gt;

Доступный функционал:

📅 Планирование поста
✍ Добавление каналов для рассылок
📑 Просмотр контент плана
📤 Рассылка по пользователям бота
📤 Рассылка в каналы


&lt;b&gt;&lt;i&gt;Важно!&lt;/i&gt;&lt;/b&gt;
&lt;i&gt;Перед началом работы проверьте и укажите корректный часовой пояс в настройках.&lt;/i&gt;"""]: ...


class StartCreate:
    @staticmethod
    def post() -> Literal["""Создать пост"""]: ...

    @staticmethod
    def description() -> Literal["""Создать описание"""]: ...


class StartMy:
    @staticmethod
    def posts() -> Literal["""Запланированные посты"""]: ...


class StartAdd:
    @staticmethod
    def channel() -> Literal["""Мои каналы"""]: ...


class Cr:
    select: CrSelect
    watch: CrWatch
    invalid: CrInvalid
    not_: CrNot_
    reply: CrReply
    edit: CrEdit
    url: CrUrl
    set: CrSet
    unset: CrUnset
    add: CrAdd
    remove: CrRemove
    push: CrPush
    instruction: CrInstruction
    approve: CrApprove
    success: CrSuccess


class CrSelect:
    channel: CrSelectChannel
    bot: CrSelectBot
    channels: CrSelectChannels


class CrSelectChannel:
    to: CrSelectChannelTo


class CrSelectChannelTo:
    send: CrSelectChannelToSend


class CrSelectChannelToSend:
    @staticmethod
    def message() -> Literal["""Выберите место публикации вашего поста. 

&lt;i&gt;Общая рассылка — это рассылка сообщения по пользователям бота&lt;/i&gt;"""]: ...


class CrSelectBot:
    to: CrSelectBotTo


class CrSelectBotTo:
    send: CrSelectBotToSend


class CrSelectBotToSend:
    @staticmethod
    def message() -> Literal["""🤖 Общая рассылка"""]: ...


class CrWatch:
    @staticmethod
    def text() -> Literal["""✍ Отправьте текст поста, который необходимо опубликовать"""]: ...


class CrInvalid:
    @staticmethod
    def data() -> Literal["""❌ Не поддерживаю такой тип данных ❌"""]: ...


class CrNot_:
    handle: CrNot_Handle


class CrNot_Handle:
    media: CrNot_HandleMedia


class CrNot_HandleMedia:
    group: CrNot_HandleMediaGroup


class CrNot_HandleMediaGroup:
    @staticmethod
    def msg() -> Literal["""Медиа группы не поддерживаются. Отправьте 1 фото или 1 видео."""]: ...


class CrReply:
    @staticmethod
    def text() -> Literal["""👆 Проверьте текст, перед публикацей"""]: ...


class CrEdit:
    scheduled: CrEditScheduled

    @staticmethod
    def text() -> Literal["""✍Изменить текст"""]: ...


class CrUrl:
    @staticmethod
    def btns() -> Literal["""☑️URL Кнопки"""]: ...

    @staticmethod
    def delete() -> Literal["""❌ Удалить кнопки"""]: ...


class CrSet:
    @staticmethod
    def time() -> Literal["""🕙Время отправки"""]: ...

    @staticmethod
    def notify() -> Literal["""🔔С уведомлением"""]: ...

    @staticmethod
    def spoiler() -> Literal["""Спойлер включен"""]: ...


class CrUnset:
    @staticmethod
    def notify() -> Literal["""🔕Без уведомления"""]: ...

    @staticmethod
    def spoiler() -> Literal["""Спойлер выключен"""]: ...

    @staticmethod
    def comments() -> Literal["""☑️Отключить комментарии"""]: ...


class CrAdd:
    @staticmethod
    def media() -> Literal["""➕Добавить медиа"""]: ...


class CrRemove:
    @staticmethod
    def media() -> Literal["""❌Удалить медиа"""]: ...


class CrPush:
    later: CrPushLater

    @staticmethod
    def now() -> Literal["""🚀Отправить сейчас"""]: ...


class CrPushLater:
    button: CrPushLaterButton

    @staticmethod
    def __call__() -> Literal["""📅Запланировать пост"""]: ...

    @staticmethod
    def message(*, current_date) -> Literal["""Планирование поста на &lt;b&gt; { $current_date } &lt;/b&gt;

Нажмите &lt;b&gt;Планировать 📌&lt;/b&gt;, чтобы подтвердить и запланировать пост в каналы:"""]: ...


class CrInstruction:
    delayed: CrInstructionDelayed
    invalid: CrInstructionInvalid
    too: CrInstructionToo
    media: CrInstructionMedia

    @staticmethod
    def url() -> Literal["""⚠ Отправьте кнопки в формате:
Link - https://ya.ru | Link 2 - https://no.com
Link 3 - http://ac.ru | Link 4 - http://mail.ru

Каждую новую кнопку отправьте с новой строки.
Если хотите разместить несколько кнопок в одной строке используйте разделитель « | »"""]: ...


class CrInstructionDelayed:
    @staticmethod
    def post(*, tz) -> Literal["""&lt;b&gt;Отправьте время выхода поста в часовом поясе { $tz } в любом удобном формате, например:&lt;/b&gt;
&lt;blockquote&gt;
18 - текущие сутки 18:00
0830 - текущие сутки 08:30
08 30 - текущие сутки 08:30
1830 - текущие сутки 18:30
18300408 - 18:30 04.08
18 30 04 08 - 18:30 04.08
&lt;/blockquote&gt;"""]: ...


class CrInstructionInvalid:
    @staticmethod
    def time(*, tz) -> Literal["""Не поддерживаю такой формат ввода данных 🤷‍♂️
&lt;b&gt;Отправьте время выхода поста в часовом поясе { $tz } в любом удобном формате, например:&lt;/b&gt;
&lt;blockquote&gt;
18 - текущие сутки 18:00
0830 - текущие сутки 08:30
08 30 - текущие сутки 08:30
1830 - текущие сутки 18:30
18300408 - 18:30 04.08
18 30 04 08 - 18:30 04.08
&lt;/blockquote&gt;"""]: ...


class CrInstructionToo:
    late: CrInstructionTooLate


class CrInstructionTooLate:
    @staticmethod
    def time() -> Literal["""Время выхода поста не может быть в прошлом."""]: ...


class CrInstructionMedia:
    invalid: CrInstructionMediaInvalid

    @staticmethod
    def post() -> Literal["""📷 Пришлите медиа файлы"""]: ...

    @staticmethod
    def approve() -> Literal["""Все медиа файлы отправлены ❓"""]: ...

    @staticmethod
    def yes() -> Literal["""✅ Да"""]: ...

    @staticmethod
    def no() -> Literal["""❌ Нет"""]: ...


class CrInstructionMediaInvalid:
    @staticmethod
    def type() -> Literal["""❌ Не поддерживаю такой тип данных ❌  
Допустимые форматы:
- Фото
- Видео"""]: ...


class CrSelectChannels:
    to: CrSelectChannelsTo


class CrSelectChannelsTo:
    push: CrSelectChannelsToPush


class CrSelectChannelsToPush:
    @staticmethod
    def message() -> Literal["""Выберите каналы для публикации поста."""]: ...


class CrApprove:
    media: CrApproveMedia


class CrApproveMedia:
    push: CrApproveMediaPush


class CrApproveMediaPush:
    @staticmethod
    def now() -> Literal["""Отправить сейчас?"""]: ...


class CrPushLaterButton:
    @staticmethod
    def caption() -> Literal["""Планировать 📌"""]: ...


class CrSuccess:
    pushed: CrSuccessPushed
    send: CrSuccessSend


class CrSuccessPushed:
    @staticmethod
    def channel(*, post_message, date_posting) -> Literal["""Пост:

 &#34;{ $post_message }&#34;

успешно запланирован на &lt;b&gt;{ $date_posting }&lt;/b&gt;
в каналах:

&lt;i&gt;При нажатии на кнопку &lt;u&gt;&lt;b&gt;Изменить пост&lt;/b&gt;&lt;/u&gt; текст, старый пост будет автоматически отменен&lt;/i&gt;"""]: ...


class CrEditScheduled:
    post: CrEditScheduledPost


class CrEditScheduledPost:
    @staticmethod
    def btn() -> Literal["""Изменить пост"""]: ...


class CrSuccessSend:
    bot: CrSuccessSendBot


class CrSuccessSendBot:
    @staticmethod
    def subscribers(*, post_message, date_posting, count_people, count_user) -> Literal["""Рассылка с материалом &#34;{ $post_message }&#34;
успешно запланирована на &lt;b&gt;{ $date_posting }&lt;/b&gt;

Количество получателей: &lt;b&gt;{ $count_people }&lt;/b&gt; { $count_user -&gt;
[1] юзер
*[other] юзеров
}"""]: ...


class Channel:
    add: ChannelAdd
    _not: Channel_not
    instruction: ChannelInstruction
    link: ChannelLink
    settings: ChannelSettings
    delete: ChannelDelete
    success: ChannelSuccess
    unsuccessful: ChannelUnsuccessful
    caption: ChannelCaption

    @staticmethod
    def exists() -> Literal["""Ниже представлен список ваших каналов."""]: ...


class ChannelAdd:
    channel: ChannelAddChannel

    @staticmethod
    def caption() -> Literal["""✍ Добавить автоподпись"""]: ...


class ChannelAddChannel:
    @staticmethod
    def button() -> Literal["""Добавить канал"""]: ...


class Channel_not:
    @staticmethod
    def exists() -> Literal["""У вас не добавлен ни один канал."""]: ...


class ChannelInstruction:
    @staticmethod
    def add() -> Literal["""Для добавления бота сделайте бота администратором в канале и дайте ему права на управление сообщениями и управление историями. 
После добавления бота отправьте ссылку на канал в формате &lt;b&gt;@channelusername&lt;/b&gt;"""]: ...


class ChannelLink:
    wrong: ChannelLinkWrong
    after: ChannelLinkAfter

    @staticmethod
    def addition() -> Literal["""https://t.me/saler_scheduler_bot?startchannel&amp;admin=post_messages+edit_messages+delete_messages+invite_users"""]: ...

    @staticmethod
    def invalid() -> Literal["""Что-то не так с ссылкой на канал, проверьте её и отправьте в формате &lt;b&gt;@channelusername&lt;/b&gt;"""]: ...


class ChannelLinkWrong:
    @staticmethod
    def type() -> Literal["""🤖 Бот может работать только с каналами. 
Типы приватных чатов, групп и форумов не поддерживаются."""]: ...


class ChannelLinkAfter:
    joining: ChannelLinkAfterJoining


class ChannelLinkAfterJoining:
    @staticmethod
    def channel() -> Literal["""🙌 Бот успешно добавлен в администраторы канала."""]: ...


class ChannelSettings:
    @staticmethod
    def desc(*, channel_name, caption) -> Literal["""🛠 Настройки канала &lt;b&gt;{ $channel_name }&lt;/b&gt;

Подпись: { $caption }"""]: ...


class ChannelDelete:
    _from: ChannelDelete_from
    channel: ChannelDeleteChannel

    @staticmethod
    def button() -> Literal["""Удалить бота 🤖"""]: ...


class ChannelDelete_from:
    @staticmethod
    def bot() -> Literal["""❌ Удалить канал из телеграм бота"""]: ...


class ChannelDeleteChannel:
    @staticmethod
    def instruction() -> Literal["""⚠ Вы удаляете бота из канала ⚠

Если вы уверены нажмите &lt;b&gt;Удалить бота 🤖&lt;/b&gt;"""]: ...


class ChannelSuccess:
    @staticmethod
    def deleted() -> Literal["""Бот успешно удален"""]: ...


class ChannelUnsuccessful:
    @staticmethod
    def deleted() -> Literal["""Бот не был удален, попробуйте повторить попытку позже. 

Если проблема повторяется - напишите в техническую поддержку 💻."""]: ...


class ChannelCaption:
    _not: ChannelCaption_not

    @staticmethod
    def on() -> Literal["""✔ Автоподпись включена"""]: ...

    @staticmethod
    def off() -> Literal["""❌ Автоподпись выключена"""]: ...

    @staticmethod
    def error() -> Literal["""📝В качестве подписи к тексту принимается только текст."""]: ...

    @staticmethod
    def wait() -> Literal["""Пришлите новую подпись к постам"""]: ...


class ChannelCaption_not:
    @staticmethod
    def exists() -> Literal["""У этого канала на данный момент нет автоподписи"""]: ...


class Content:
    bot: ContentBot
    channel: ContentChannel
    today: ContentToday
    month: ContentMonth
    process: ContentProcess
    successfull: ContentSuccessfull
    unsuccessful: ContentUnsuccessful

    @staticmethod
    def hello() -> Literal["""Выберите раздел, где хотите посмотреть контент план."""]: ...


class ContentBot:
    @staticmethod
    def btn() -> Literal["""Подписчики бота"""]: ...


class ContentChannel:
    @staticmethod
    def btn() -> Literal["""Каналы"""]: ...


class ContentToday:
    info: ContentTodayInfo


class ContentTodayInfo:
    @staticmethod
    def msg(*, selected_date, type_, count_post) -> Literal["""На &lt;b&gt;{ $selected_date }&lt;/b&gt; в { $type_ -&gt;
[bot] рассылке по подписчикам
[channel] рассылке по каналам
*[other] { $type_ }
*[other]  рассылке
}
{ $count_post -&gt;
[0] &lt;u&gt;нет запланированных новостей&lt;/u&gt;
[one] 1 запланированное сообщение
*[other] { $count_post }
*[other]  запланированных сообщений
}"""]: ...


class ContentMonth:
    info: ContentMonthInfo


class ContentMonthInfo:
    @staticmethod
    def msg(*, month, type_, count_post) -> Literal["""На &lt;b&gt;{ $month }&lt;/b&gt; в { $type_ -&gt;
[bot] рассылке по подписчикам
[channel] рассылке по каналам
*[other] { $type_ }
*[other]  рассылке
} рассылке по подписчикам { $count_post -&gt;
[0] &lt;u&gt;нет запланированных новостей&lt;/u&gt;
[one] 1 запланированное сообщение
*[other] { $count_post }
*[other]  запланированных сообщений
}"""]: ...


class ContentProcess:
    select: ContentProcessSelect


class ContentProcessSelect:
    post: ContentProcessSelectPost


class ContentProcessSelectPost:
    @staticmethod
    def msg() -> Literal["""Для отмены запланированного поста нажмите &lt;b&gt;✋ Отменить&lt;/b&gt;."""]: ...


class ContentSuccessfull:
    @staticmethod
    def deleted() -> Literal["""Запланированный пост был успешно отменен."""]: ...


class ContentUnsuccessful:
    @staticmethod
    def deleted() -> Literal["""Не удалось отменить пост. 

Попробуйте, перезапустить бота по кнопке &lt;a href=&#34;/start&#34;&gt;/start&lt;/a&gt; и повторите попытку."""]: ...


class Settings:
    main: SettingsMain
    timezone: SettingsTimezone
    support: SettingsSupport
    select: SettingsSelect


class SettingsMain:
    @staticmethod
    def menu() -> Literal["""&lt;b&gt;Настройки&lt;/b&gt;

Настройте конфигурацию вашего бота."""]: ...


class SettingsTimezone:
    @staticmethod
    def button() -> Literal["""🌍 Часовой пояс"""]: ...


class SettingsSupport:
    @staticmethod
    def button() -> Literal["""🤝 Онлайн-поддержка"""]: ...

    @staticmethod
    def message() -> Literal["""Для вопросов и предложений: &lt;a href=&#34;@inactive0073&#34;&gt;@inactive0073&lt;/a&gt;

Всегда открыты и заинтересованы в решении ваших задач!"""]: ...


class SettingsSelect:
    @staticmethod
    def timezone(*, current_timezone, local_datetime) -> Literal["""Выберете ваш часовой пояс.

Ваш выбранный часовой пояс: &lt;b&gt;{ $current_timezone }&lt;/b&gt;.
Локальное время: &lt;b&gt;{ $local_datetime }&lt;/b&gt;"""]: ...


class Admin:
    not_: AdminNot_
    comeback: AdminComeback
    hello: AdminHello
    ban: AdminBan
    role: AdminRole
    reports: AdminReports
    team: AdminTeam


class AdminNot_:
    found: AdminNot_Found


class AdminNot_Found:
    @staticmethod
    def user() -> Literal["""Пользователь не найден. Проверьте данные и попробуйте еще раз. Убедитесь, что он завершил регистрацию как клиент.

Допустимый формат поиска: &lt;b&gt;123455&lt;/b&gt;, если ищем по Telegram ID или &lt;b&gt;@username&lt;/b&gt;, если ищем по имени пользователя."""]: ...


class AdminComeback:
    @staticmethod
    def btn() -> Literal["""🔙 В админ меню"""]: ...


class AdminHello:
    @staticmethod
    def message() -> Literal["""Ваша роль: &lt;b&gt;Администратор&lt;/b&gt;

Доступный функционал:

📱 Функционал менеджера
👨‍💼 Управление командой
📃 Отчет системы лояльности персонала"""]: ...


class AdminBan:
    menu: AdminBanMenu
    not_: AdminBanNot_
    success: AdminBanSuccess
    unban: AdminBanUnban

    @staticmethod
    def ban() -> Literal["""Заблокировать"""]: ...


class AdminBanMenu:
    @staticmethod
    def btn() -> Literal["""Блокировка/разблокировка"""]: ...

    @staticmethod
    def msg() -> Literal["""Напишите &lt;b&gt;ID телеграм&lt;/b&gt; пользователя или &lt;b&gt;@username&lt;/b&gt;."""]: ...


class AdminRole:
    customer: AdminRoleCustomer
    waiter: AdminRoleWaiter
    manager: AdminRoleManager


class AdminRoleCustomer:
    @staticmethod
    def btn() -> Literal["""Клиент"""]: ...


class AdminRoleWaiter:
    @staticmethod
    def btn() -> Literal["""Официант"""]: ...


class AdminRoleManager:
    @staticmethod
    def btn() -> Literal["""Менеджер"""]: ...


class AdminReports:
    menu: AdminReportsMenu
    all_: AdminReportsAll_
    bonus: AdminReportsBonus

    @staticmethod
    def btn() -> Literal["""Отчеты"""]: ...


class AdminTeam:
    menu: AdminTeamMenu
    invite: AdminTeamInvite
    select: AdminTeamSelect
    already: AdminTeamAlready
    kick: AdminTeamKick
    approve: AdminTeamApprove

    @staticmethod
    def btn() -> Literal["""Команда"""]: ...


class AdminReportsMenu:
    @staticmethod
    def msg() -> Literal["""Выберите отчет для просмотра"""]: ...


class AdminReportsAll_:
    users: AdminReportsAll_Users
    scheduled_posts: AdminReportsAll_Scheduled_posts


class AdminReportsAll_Users:
    @staticmethod
    def btn() -> Literal["""Выгрузить клиентов"""]: ...


class AdminReportsBonus:
    accrual: AdminReportsBonusAccrual


class AdminReportsBonusAccrual:
    records: AdminReportsBonusAccrualRecords


class AdminReportsBonusAccrualRecords:
    @staticmethod
    def btn() -> Literal["""Выгрузить записи начисления бонусов"""]: ...


class AdminReportsAll_Scheduled_posts:
    @staticmethod
    def btn() -> Literal["""Выгрузить запланированные посты"""]: ...


class AdminTeamMenu:
    @staticmethod
    def msg() -> Literal["""Выберите подходящий пункт из меню."""]: ...


class AdminTeamInvite:
    @staticmethod
    def btn() -> Literal["""Добавить в команду"""]: ...

    @staticmethod
    def msg() -> Literal["""Отправьте @username или Telegram ID пользователя. 

&lt;i&gt;Перед добавлением в команду пользователь должен запустить бота. Без этого вы не сможете добавить его в команду.&lt;/i&gt;"""]: ...

    @staticmethod
    def success() -> Literal["""Пользователь был успешно добавлен в команду."""]: ...

    @staticmethod
    def unsuccess() -> Literal["""Не удалось добавить пользователя в команду. Попробуйте позже, если ошибка повторяется обратитесь в службу поддержки."""]: ...


class AdminTeamSelect:
    role: AdminTeamSelectRole


class AdminTeamSelectRole:
    @staticmethod
    def msg() -> Literal["""Выберите роль для члена вашей команды."""]: ...


class AdminTeamAlready:
    has: AdminTeamAlreadyHas


class AdminTeamAlreadyHas:
    @staticmethod
    def roles() -> Literal["""У этого пользователя уже есть все роли."""]: ...


class AdminTeamKick:
    @staticmethod
    def btn() -> Literal["""Удалить из команды"""]: ...

    @staticmethod
    def msg() -> Literal["""Выберите пользователей для удаления."""]: ...

    @staticmethod
    def success() -> Literal["""Пользователи были успешно удалены из команды."""]: ...

    @staticmethod
    def unsuccess() -> Literal["""Не удалось удалить сотрудников. Попробуйте, пожалуйста, позже."""]: ...


class AdminTeamApprove:
    kick: AdminTeamApproveKick


class AdminTeamApproveKick:
    @staticmethod
    def msg() -> Literal["""Вы уверены, что хотите удалить из команды выбранных пользователей? 

&lt;i&gt;Удаление из команды никак не повлияет на их профиль клиента. Они смогут пользоваться системой лояльности.&lt;/i&gt;"""]: ...


class AdminBanNot_:
    found: AdminBanNot_Found


class AdminBanNot_Found:
    @staticmethod
    def msg() -> Literal["""Пользователь не найден. Проверьте данные и попробуйте еще раз. 

Если все равно не удается найти пользователя, возможно, его нет в базе данных или он не запускал бота."""]: ...


class AdminBanSuccess:
    @staticmethod
    def msg(*, i_name, telegram_id) -> Literal["""Пользователь [{ $i_name }-{ $telegram_id }] заблокирован."""]: ...


class AdminBanUnban:
    success: AdminBanUnbanSuccess

    @staticmethod
    def __call__() -> Literal["""Разблокировать"""]: ...


class AdminBanUnbanSuccess:
    @staticmethod
    def msg(*, i_name, telegram_id) -> Literal["""Пользователь [{ $i_name }-{ $telegram_id }] разблокирован."""]: ...

