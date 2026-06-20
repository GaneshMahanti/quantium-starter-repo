from app import app

def test_header_present():
    layout_str = str(app.layout)
    assert "Soul Foods Pink Morsel Sales Visualiser" in layout_str

def test_visualisation_present():
    layout_str = str(app.layout)
    assert "sales-chart" in layout_str

def test_region_picker_present():
    layout_str = str(app.layout)
    assert "region-picker" in layout_str
