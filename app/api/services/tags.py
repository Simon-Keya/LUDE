from typing import List

from ..models.tags import Tag


def get_all_tags() -> List[Tag]:
    return Tag.query.all()


def get_tag_by_id(tag_id: int) -> Tag:
    return Tag.query.get(tag_id)


def create_tag(tag_data: dict) -> Tag:
    tag = Tag(**tag_data)
    tag.save()
    return tag


def update_tag(tag_id: int, tag_data: dict) -> Tag:
    tag = Tag.query.get(tag_id)
    tag.update(**tag_data)
    tag.save()
    return tag


def delete_tag(tag_id: int) -> None:
    tag = Tag.query.get(tag_id)
    tag.delete()
