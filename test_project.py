import pytest
import json
import os
from project import add_task, complete_task, delete_task, save_tasks, load_tasks


def test_add_task(monkeypatch):
    """اختبار إضافة مهمة جديدة"""
    inputs = iter(["Test Task", "This is a test", "high"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    task = add_task()
    
    assert task["title"] == "Test Task"
    assert task["description"] == "This is a test"
    assert task["priority"] == "high"
    assert task["status"] == "pending"
    assert task["created_at"] is not None


def test_complete_task():
    """اختبار تعليم مهمة كمكتملة"""
    tasks = [
        {"id": "1", "title": "Task 1", "status": "pending", "created_at": "2024-01-01", "completed_at": None}
    ]
    
    result = complete_task(tasks, "1")
    assert result == True
    assert tasks[0]["status"] == "completed"
    assert tasks[0]["completed_at"] is not None
    
    result = complete_task(tasks, "999")
    assert result == False


def test_delete_task():
    """اختبار حذف مهمة"""
    tasks = [
        {"id": "1", "title": "Task 1"},
        {"id": "2", "title": "Task 2"}
    ]
    
    result = delete_task(tasks, "1")
    assert result == True
    assert len(tasks) == 1
    assert tasks[0]["id"] == "2"
    
    result = delete_task(tasks, "999")
    assert result == False


def test_save_and_load_tasks():
    """اختبار حفظ وتحميل المهام"""
    tasks = [
        {"id": "1", "title": "Test Task", "status": "pending"}
    ]
    
    save_tasks(tasks)
    
    loaded_tasks = load_tasks()
    assert len(loaded_tasks) == len(tasks)
    assert loaded_tasks[0]["title"] == tasks[0]["title"]
    
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")


def test_complete_task_already_completed():
    """اختبار تعليم مهمة مكتملة بالفعل"""
    tasks = [
        {"id": "1", "title": "Task 1", "status": "completed", "created_at": "2024-01-01", "completed_at": "2024-01-02"}
    ]
    
    result = complete_task(tasks, "1")
    assert result == False
    assert tasks[0]["status"] == "completed"


def test_add_task_default_priority(monkeypatch):
    """اختبار إضافة مهمة بأولوية افتراضية"""
    inputs = iter(["Test Task", "", ""])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    task = add_task()
    
    assert task["priority"] == "medium"


def test_add_task_empty_title(monkeypatch):
    """اختبار منع إضافة مهمة بدون عنوان"""
    inputs = iter(["", "Valid Title", "Description", "low"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    task = add_task()
    
    assert task["title"] == "Valid Title"
