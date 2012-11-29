from polls.models import Poll
from django.contrib import admin
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
        fieldsets = [
                (None,               {'fields': ['question']}),
                ('Date information', {'fields': ['pub_date']}),
        ]
        inlines = [ChoiceInline]
        list_display = ('question', 'pub_date', 'was_published_recently')

admin.site.register(Poll, PollAdmin)

#class PollAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question']

#admin.site.register(Poll, PollAdmin)


#admin.site.register(Poll)



