from django.contrib import admin

# importation des models.
from . import models
from django.utils.safestring import mark_safe
# Register your models here.
class SousCategorieInline(admin.TabularInline):
    model = models.SousCategorie
    extra = 0



@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('view_image','nom','status','date_add','date_upd')
    list_filter = ('status','date_add','date_upd')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    actions = ('active','desactive')
    list_display_links = ['nom','view_image']
    list_per_page = 3
    ordering = ['nom']
    inlines = [SousCategorieInline]
    readonly_fields = ['detail_image']
    
    def view_image(self,obj):
        return mark_safe('<img src = "{url}" width = " 100px " heigth = " 100px " />'.format(url=obj.image.url)) 
       
    def detail_image(self,obj):
        return mark_safe('<img src = "{url}" width = " 100px " heigth = " 100px " />'.format(url=obj.image.url))
    
    
        
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
        
    active.short_description = "activer Les sousCategorie selectionnés"
        
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
            
    desactive.short_description = "desactivés Les sousCategorie selectionnés"
        
    
    
@admin.register(models.SousCategorie)
class SousCategorieAdmin(admin.ModelAdmin):
    list_display = ('categorie','nom','status','date_add','date_upd','view_image')
    list_filter = ('categorie','status','date_add','date_upd')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    actions = ('active','desactive')
    list_display_links = ['nom','view_image']
    list_per_page = 3
    ordering = ['nom']
    readonly_fields = ['detail_image']
    
    # creation des fonction
    
    def view_image(self,obj):
       return mark_safe('<img src = "{url}" width = " 250px " heigth = " 350px " />'.format(url=obj.image.url))
   
    def detail_image(self,obj):
        return mark_safe('<img src = "{url}" width = " 100px " heigth = " 100px " />'.format(url=obj.image.url))
    
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les sousCategorie selectionnés"
    
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les sousCategorie selectionnés"
    
    
@admin.register(models.Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('souscategorie','titre','status','date_add','date_upd','view_image')
    list_filter = ('souscategorie','status','date_add','date_upd')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    actions = ('active','desactive')
    list_display_links = ['titre','view_image']
    list_per_page = 3
    ordering = ['titre']
    filter_horizontal = ('tag',)
    readonly_fields = ['detail_image']
    fieldsets = [
        ('Titre et Visibilité',{
            'fields':['titre','status']
        }),
        ('Description et image',{
            'fields':['descriprion','image']
        }),
        ('tags et sous Categorie',{
            'fields':['tag','souscategorie']
        })
    ]
    
    
    # creation des fonction
    def view_image(self,obj):
        return mark_safe('<img src = "{url}" width = " 250px " heigth = " 350px " />'.format(url=obj.image.url))
   
    def detail_image(self,obj):
        return mark_safe('<img src = "{url}" width = " 100px " heigth = " 100px " />'.format(url=obj.image.url))

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les sousCategorie selectionnés"
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les sousCategorie selectionnés"
    
    
    
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nom','status','date_add','date_upd')
    list_filter = ('status','date_add','date_upd')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    actions = ('active','desactive')
    list_per_page = 3
    ordering = ['nom']
    
    # creation des fonction
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les sousCategorie selectionnés"
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les sousCategorie selectionnés"