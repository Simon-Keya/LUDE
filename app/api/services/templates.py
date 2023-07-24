# templates.py
from typing import List

from ..models.templates import Template


def get_all_templates() -> List[Template]:
    return Template.query.all()


def get_template_by_id(template_id: int) -> Template:
    return Template.query.get(template_id)


def create_template(template_data: dict) -> Template:
    template = Template(**template_data)
    template.save()
    return template


def update_template(template_id: int, template_data: dict) -> Template:
    template = Template.query.get(template_id)
    template.update(**template_data)
    template.save()
    return template


def delete_template(template_id: int) -> None:
    template = Template.query.get(template_id)
    template.delete()
