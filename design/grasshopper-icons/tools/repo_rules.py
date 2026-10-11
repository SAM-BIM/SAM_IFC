"""Repository-specific classification decisions for SAM_IFC (the only non-shared tool file).

OVERRIDES     : component display name -> (object glyph, op, extra)   extra: None | "plural" | "library" | note
PARAM_OBJECTS : param type key (Goo<X>Param class or typeof(X) name) -> glyph | (glyph, container, plural)
OBJECTS/VERBS : extra noun/verb rules tried before the shared ones (same shapes as SAM's OBJECTS/VERBS)
"""
OVERRIDES = {
    "SAMAnalytical.IFC": ("object", "export", None), "IFC.Open": ("file", "import", None), "IFC.Save": ("file", "export", None),
}
PARAM_OBJECTS = {"IfcStore": "file", "GooIfcStore": "file"}
OBJECTS = []
VERBS = []
