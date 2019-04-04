from django.contrib import admin
from core.models import Category, Deck, Card, Quiz
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name',)

@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ('title', 'public')

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
   pass
