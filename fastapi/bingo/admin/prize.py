from django.contrib import admin, messages
from django.shortcuts import redirect
from django.urls import path, reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from ..models import Prize


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "preview",
        "count",
        "plus_count_button",
        "minus_count_button",
    )
    search_fields = ("name",)

    # Preview
    def preview(self, instance):
        style = "width:5rem; height:auto;"
        tag = '<a href="{}"><img src="{}" style="{}"/></a>'
        if instance.image and hasattr(instance.image, "url"):
            return mark_safe(tag.format(instance.image.url, instance.image.url, style))
        return None

    preview.short_description = "preview"

    # Plus and Minus
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "<uuid:uuid>/plus_count/",
                self.admin_site.admin_view(self.plus_count),
                name="plus_count",
            ),
            path(
                "<uuid:uuid>/minus_count/",
                self.admin_site.admin_view(self.minus_count),
                name="minus_count",
            ),
        ]
        return custom_urls + urls

    # Plus
    def plus_count_button(self, obj):
        return mark_safe(
            format_html(
                '<a class="button" href="{}">Plus</a>',
                reverse("admin:plus_count", args=[obj.uuid]),
            )
        )

    plus_count_button.short_description = "Plus"
    plus_count_button.allow_tags = True

    def plus_count(self, request, uuid):
        prize = Prize.objects.get(uuid=uuid)
        prize.count += 1
        prize.save()
        return redirect(reverse("admin:bingo_prize_changelist"))

    # Minus
    def minus_count_button(self, obj):
        return mark_safe(
            format_html(
                '<a class="button" href="{}">Minus</a>',
                reverse("admin:minus_count", args=[obj.uuid]),
            )
        )

    minus_count_button.short_description = "Minus"
    minus_count_button.allow_tags = True

    def minus_count(self, request, uuid):
        prize = Prize.objects.get(uuid=uuid)
        if prize.count > 0:
            prize.count -= 1
            prize.save()
        else:
            messages.error(request, "Count must be greater than 0.")
        return redirect(reverse("admin:bingo_prize_changelist"))
