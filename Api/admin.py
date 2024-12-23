from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('username', 'password',)
    list_display = ('username', 'password', )
    
class TokenAdmin(admin.ModelAdmin):
    exclude = ('token',)
    list_display = ('user', 'created_at', )
    readonly_fields = ('user', 'created_at', 'token',)
    
    
class ChatAdmin(admin.ModelAdmin):
    readonly_fields = ('user','message', 'response', 'timestamp', )
    list_display = ('user', 'message', 'timestamp', )

admin.site.register(User, UserAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Token, TokenAdmin)