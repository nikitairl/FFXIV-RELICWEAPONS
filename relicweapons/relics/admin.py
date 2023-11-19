from django.contrib import admin

from . models import RelicWeapon, Quest, Reward


class RelicWeaponAdmin(admin.ModelAdmin):
    list_display = ('relic_type', 'weapon_name', 'job', 'text',)
    save_as = True


class QuestAdmin(admin.ModelAdmin):
    list_display = ('quest_name', 'step', 'location', 'reward',)
    save_as = True


class RewardAdmin(admin.ModelAdmin):
    list_display = ('reward_name', 'description', )


admin.site.register(RelicWeapon, RelicWeaponAdmin)
admin.site.register(Quest, QuestAdmin)
admin.site.register(Reward, RewardAdmin)
