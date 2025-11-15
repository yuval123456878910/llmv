; ModuleID = "MAIN"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"2Cal" = sdiv i32 10, 2
  %"Cal2" = alloca i32
  store i32 %"2Cal", i32* %"Cal2"
  %"3Cal" = load i32, i32* %"Cal2"
  ret i32 %"3Cal"
}
