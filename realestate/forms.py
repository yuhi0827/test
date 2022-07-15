# from django import forms
# from django.core.mail import BadHeaderError, send_mail
# from django.http import HttpResponse

# class ContactForm(forms.Form):
#     subject = forms.CharField(
#         label="件名",
#         max_length=100, 
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "件名",
#             }
#         )
#     )

#     message = forms.CharField(
#         label="問い合わせ内容",
#         widget=forms.Textarea(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "問い合わせ内容"
#             }
#         )
#     )

#     def send_email(self, username, email):
#         subject = "【お問い合わせ" + self.cleaned_data["subject"]
#         message = self.cleaned_data["message"] + f"\n\nBy {username}."
#         recipient_list = ["yuhi.kikake@gmail.com"]   ### 送信先
#         try:
#             send_mail(subject, message, email, recipient_list)
#         except BadHeaderError:
#             return HttpResponse("無効なヘッダが検出されました。")