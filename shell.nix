# This allows overriding pkgs by passing `--arg pkgs ...`
{ pkgs ? import <nixpkgs> {}, pinned ? null }:
with pkgs;
let

  python' = python3.override {
    packageOverrides = self: super: {

    };
  };

  python-env = python'.withPackages(pp: with pp; [
      ipython
      pip
      virtualenv
      pylint
      autopep8
      numpy
      matplotlib
      tqdm
  ]);


in
mkShell {
  name = "google-hashcode-env";
  buildInputs = [
    # put packages here.
    python-env
  ];

  shellHook = ''
  '';
}
