/ basic logging for a q process
.log.out:{[x] show string[.z.T]," | " sv (enlist ""),x;};
.z.pg:{.log.out ("sync";string[.z.w];x);value x};
.z.po:{.log.out ("Opening";string[.z.w])};
.z.pc:{.log.out ("Closing";string[x])};

system "p 5000"