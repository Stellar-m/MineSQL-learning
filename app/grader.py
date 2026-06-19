from collections import Counter


def grade(student_rows, reference_rows, order_matters=False):
    if order_matters:
        if student_rows == reference_rows:
            return _result("correct", None, [], [], student_rows, reference_rows)

        missing, unexpected = _multiset_diff(student_rows, reference_rows)
        if not missing and not unexpected:
            diff_type = "wrong_order"
        else:
            diff_type = _classify(missing, unexpected)
        return _result("incorrect", diff_type, missing, unexpected, student_rows, reference_rows)

    missing, unexpected = _multiset_diff(student_rows, reference_rows)
    if not missing and not unexpected:
        return _result("correct", None, [], [], student_rows, reference_rows)
    return _result("incorrect", _classify(missing, unexpected), missing, unexpected, student_rows, reference_rows)


def _multiset_diff(student_rows, reference_rows):
    ref = Counter(reference_rows)
    stu = Counter(student_rows)
    missing = list((ref - stu).elements())
    unexpected = list((stu - ref).elements())
    return missing, unexpected


def _classify(missing, unexpected):
    if missing and not unexpected:
        return "missing_rows"
    if unexpected and not missing:
        return "unexpected_rows"
    return "mismatch"


def _result(verdict, diff_type, missing, unexpected, student_rows, reference_rows):
    return {
        "verdict": verdict,
        "diff_type": diff_type,
        "missing_rows": missing,
        "unexpected_rows": unexpected,
        "row_count_student": len(student_rows),
        "row_count_reference": len(reference_rows),
    }
