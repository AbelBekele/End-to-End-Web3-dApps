import pytest
from unittest.mock import patch, MagicMock
from utils import create_certificate, pin_file_to_ipfs

@patch('utils.cv2')
@patch('utils.os')
def test_create_certificate(mock_os, mock_cv2):
    mock_os.getenv.return_value = 'test_jwt'
    mock_cv2.imread.return_value = 'test_image'
    mock_cv2.imwrite.return_value = True
    full_name = 'Test Name'
    date = '2022-01-01'
    week = 'Week 1'
    with patch('utils.pin_file_to_ipfs') as mock_pin_file:
        mock_pin_file.return_value = 'test_hash'
        result = create_certificate(full_name, date, week)
    assert result == 'test_hash'

@patch('utils.requests')
def test_pin_file_to_ipfs(mock_requests):
    mock_requests.post.return_value = MagicMock(status_code=200, json=lambda: {"IpfsHash": "test_hash"})
    filename = 'test_file'
    result = pin_file_to_ipfs(filename)
    assert result == 'test_hash'