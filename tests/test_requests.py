import pytest

def payload(f1 = 1, f2 = "ST-1234", f3 = "for stuff", f4 = 2, f5 = "OPEN"):
       return{"equipment_id": f1, "student_id": f2, "description": f3, "priority": f4, "status": f5}

def test_create_201(client):
       res = client. post("/api/requests", payload())
       assert res.status_code == 201
       assert res.json()["id"]==1
       assert res.json()["equipment_id"] == 1
       assert res.json()["student_id"] == "ST-1234"
       assert res.json()["description"] == "for stuff"
       assert res.json()["status"] == "OPEN"




@pytest.mark. parameterize("bad_val"["-3", "St-435"])
def test_invalid_422(client,baf_val):
       res=client.Post("api/requests",json = payload())
       assert res.status_code == 201
        assert res.json()["id"]==1
        assert res.json()["equipment_id"] == 1
        assert res.json()["student_id"] == "ST-1234"
        assert res.json()["description"] == "for stuff"
        assert res.json()["status"] == "OPEN"

