import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class HideGroupsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IFacets, inherit=True)
    plugins.implements(plugins.IAuthFunctions, inherit=True)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')

    # IFacets

    def _facets(self, facets_dict):
        if 'groups' in facets_dict:
            del facets_dict['groups']
        return facets_dict

    def dataset_facets(self, facets_dict, package_type):
        return self._facets(facets_dict)

    def group_facets(self, facets_dict, group_type, package_type):
        return self._facets(facets_dict)

    def organization_facets(self, facets_dict, organization_type,
                            package_type):
        return self._facets(facets_dict)

    # IAuthFunctions

    def get_auth_functions(self):
        return {'group_create': _group_create}


def _group_create(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to create groups'}
