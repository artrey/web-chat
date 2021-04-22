document.addEventListener('DOMContentLoaded', function () {
  for (const textarea of document.querySelectorAll('textarea')) {
    const textareaCopy = textarea;
    textarea.onkeydown = function (e) {
      if (e.code === 'Enter' && !e.shiftKey) {
        if (textareaCopy.textLength > 0) {
          textareaCopy.parentElement.submit();
        }
        return false;
      }
      return true;
    }
  }

  const textareas = document.querySelectorAll('textarea');
  if (textareas.length > 0) {
    textareas[textareas.length - 1].focus();
  }
});
