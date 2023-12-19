import typing
from render_engine.plugins import hook_impl

class {{cookiecutter.project_slug|capitalize}}:
    default_settings: {"default_setting": "default_value"}
    
    {% if cookiecutter.pre_build_site %}
    @hook_spec
    def pre_build_site(
        self,
        site,
        settings: dict[str, typing.Any],
    ) -> None:
        """Steps Prior to Building the site"""
        pass
    {% endif %}
    {% if cookiecutter.post_build_site %}
    @hook_spec
    def post_build_site(
        self,
        site,
    ) -> None:
        """Build After Building the site"""
        pass
    {% endif %}
    {% if cookiecutter.render_content %}
    @hook_spec
    def render_content(
        self,
        page,
        settings: dict[str, typing.Any],
    ) -> None:
        """
        Augments the content of the page before it is rendered as output.
        """
        pass
    {% endif %}
    {% if cookiecutter.post_render_content %}
    @hook_spec
    def post_render_content(
        self,
        page,
        settings: dict[str : typing.Any],
        site,
    ) -> None:
        """
        Augments the content of the page before it is rendered as output.
        """
        pass
    {% endif %}
    {% if cookiecutter.pre_build_collection%}
    @hook_spec
    def pre_build_collection(
        self,
        collection,
        settings: dict[str, typing.Any],
    ) -> None:
        """Steps Prior to Building the collection"""
        pass
    {% endif %}
    {% if cookiecutter.post_build_collection %}
    @hook_spec
    def post_build_collection(
        self,
        site,
        settings: dict[str, typing.Any],
    ) -> None:
        """Build After Building the collection"""
        pass
    {% endif %}