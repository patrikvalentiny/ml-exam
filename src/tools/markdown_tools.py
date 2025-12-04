import tempfile
import os
from pymarkdown.api import PyMarkdownApi, PyMarkdownScanPathResult

def verify_markdown_file(file_path: str) -> str:
    """
    Verifies if a markdown file follows standard rules using PyMarkdownApi.
    
    Args:
        file_path (str): The path to the markdown file to verify.
        
    Returns:
        str: A report of the scan results. Returns "No issues found." if the file is valid.
    """
    try:
        scan_result: PyMarkdownScanPathResult = PyMarkdownApi().scan_path(file_path)
        
        if not scan_result.scan_failures:
            return "No issues found."
            
        report = [f"Found {len(scan_result.scan_failures)} issues in {file_path}:"]
        for failure in scan_result.scan_failures:
            report.append(
                f"- Line {failure.line_number}, Column {failure.column_number}: "
                f"[{failure.rule_id}] {failure.rule_name}: {failure.extra_error_information or ''}"
            )
            
        return "\n".join(report)
        
    except Exception as e:
        return f"Error verifying markdown file: {str(e)}"

def verify_markdown_content(content: str) -> str:
    """
    Verifies if a markdown string follows standard rules using PyMarkdownApi.
    
    Args:
        content (str): The markdown content to verify.
        
    Returns:
        str: A report of the scan results. Returns "No issues found." if the content is valid.
    """
    # Create a temporary file to scan
    fd, tmp_path = tempfile.mkstemp(suffix='.md', text=True)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as tmp:
            tmp.write(content)
        
        return verify_markdown_file(tmp_path)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

