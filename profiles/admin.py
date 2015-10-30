# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from .models import User


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)

class UserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label= ("Password"),
        help_text= ("Las contraseñas no se almacenan crudas. No hay manera de ver "
                    "la contraseña de este usuario, pero puedes cambiarla "
                    "usando <a href=\"password/\">este formulario</a>."))
    class Meta(UserChangeForm.Meta):
        model = User

class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    fieldsets = (
        (None,           {'fields': ('username', 'first_name', 'last_name', 'cedula', 'email', 'phone','password','es_docente','avatar')}),
        ('Permisos',     {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'cedula', 'email', 'password1', 'password2', 'phone','es_docente',)}
        ),
    )

    list_display = ('username', 'fullname', 'email', 'cedula', 'phone', 'is_active', 'is_staff','es_docente','getimagenes',)
    list_filter = ('is_active','is_staff','es_docente', )
    search_fields = ('email', 'phone' 'cedula','first_name', 'last_name',)
    ordering = ('first_name', 'email',)
    

    def fullname(self, obj):
        return obj.get_full_name()

    fullname.short_description = 'Nombre completo'
    fullname.admin_order_field = 'first_name'


    def getimagenes(self, obj):
    	if obj.avatar:
    		return '<img src="%s" width="80px" height="80px">' % (obj.avatar.url)
    	else:
    		return '<img src="%s" width="80px" height="80px">' % ('http://placehold.it/80x80s')
	getimagenes.allow.tags = True
	getimagenes.admin_order_field = 'imagen'
	getimagenes.short_description = 'Imagen'


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)


