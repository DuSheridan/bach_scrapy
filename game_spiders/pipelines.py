# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

# Default Pipeline
# class GameSpidersPipeline:
#     def process_item(self, item, spider):
#         return item


class DjangoPipeline:
    collection_name = 'scrapy_items'

    def __init__(self, django_model):
        self.django_model = django_model

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        return cls(
            crawler.settings.get('TEST_APP_MODEL')
        )

    def process_item(self, item, spider):
        item_to_save = item
        print(item_to_save)
        try:
            new_item = self.django_model(text=item["text"])
            new_item.save()
            return new_item
        except Exception as e:
            raise DropItem(f"Item found with no text or exception occurred on saving the item: {item}")
