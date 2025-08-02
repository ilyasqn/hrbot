class Formatter:
    @staticmethod
    async def safe_line(emoji: str, label: str, value: str | None) -> str:
        return f"{emoji} {label}: {value}" if value else ""

    @classmethod
    async def format_vacancy(cls, data: dict) -> str:
        return "\n".join(filter(None, [
            await cls.safe_line("🧑‍💼", "Должность", data.get('position')),
            await cls.safe_line("🏢", "Компания", data.get('company')),
            await cls.safe_line("🔗", "Сайт компании", data.get('company_link')),
            await cls.safe_line("🏙️", "Описание компании", data.get('company_description')),
            await cls.safe_line("📍", "Локация", data.get('city')),
            f"💰 Зарплата: от {data.get('salary_from')} до {data.get('salary_to')}"
            if data.get("salary_from") and data.get("salary_to") else "",
            await cls.safe_line("📅", "Опыт", f"{data.get('experience')} лет" if data.get("experience") else ""),
            await cls.safe_line("🧭", "Формат работы", data.get('work_type')),
            await cls.safe_line("📈", "Уровень", data.get('level')),
            f"🧑‍💼 Обязанности:\n{data.get('responsibilities')}" if data.get("responsibilities") else "",
            f"📌 Требования:\n{data.get('requirements')}" if data.get("requirements") else "",
            f"📝 Описание:\n{data.get('description')}" if data.get("description") else "",
            await cls.safe_line("📞", "Контакты", data.get('contacts')),
        ]))

    @classmethod
    async def format_event(cls, data: dict) -> str:
        return "\n".join(filter(None, [
            await cls.safe_line("🎉", "Название события", data.get('name')),
            await cls.safe_line("🏢", "Организатор", data.get('company')),
            f"📝 Описание:\n{data.get('description')}" if data.get("description") else "",
            await cls.safe_line("📅", "Дата проведения", data.get('date')),
        ]))
