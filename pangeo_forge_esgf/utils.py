from typing import Dict, Optional

CMIP6_naming_schema = "mip_era.activity_id.institution_id.source_id.experiment_id.member_id.table_id.variable_id.grid_label.version"
CORDEX_naming_schema = "project.product.domain.institute.driving_model.experiment.ensemble.rcm_name.rcm_version.time_frequency.variable.version"
CORDEX_adjust_naming_schema = "project.product.domain.institute.driving_model.experiment.ensemble.rcm_name.bias_adjustment.time_frequency.variable.version"


schemes = {
    "CMIP6": CMIP6_naming_schema,
    "CORDEX": CORDEX_naming_schema,
    "CORDEX-Reklies": CORDEX_naming_schema,
    "CORDEX-ESD": CORDEX_naming_schema,
    "CORDEX-Adjust": CORDEX_adjust_naming_schema,
}


def facets_from_iid(
    iid: str, fix_version: bool = True, scheme: Optional[str] = None
) -> Dict[str, str]:
    """Translates iid string to facet dict according to CMIP6 naming scheme.
    By default removes `v` from version
    """
    if scheme is None:
        # get scheme from mip_era or project
        scheme = iid.split(".")[0]
    iid_name_template = schemes[scheme]
    template_split = iid_name_template.split(".")
    iid_split = iid.split(".")
    if len(template_split) != len(iid_split):
        raise ValueError(
            f"Found {len(iid_split)} facets in `iid`, but expected {len(template_split)}. Got {iid_split=}"
        )
    facets = {}
    for name, value in zip(template_split, iid_split):
        facets[name] = value
    if fix_version:
        facets["version"] = facets["version"].replace("v", "")
    return facets
