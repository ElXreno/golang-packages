%global goipath         github.com/Unknwon/cae/zip
%global commit          c6aac99ea2cae2ebaf23f26f76b04fe3fcfc9f8c
%global scm             git

%gometa

%global common_description %{expand:
Package cae implements PHP-like Compression and Archive Extensions
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Package cae implements PHP-like Compression and Archive Extensions

License:                Apache-2.0
URL:                    %{gourl}
Source0:                %{gosource}


%description
%{common_description}

%gopkg


%prep
%goprep


%install
%gopkginstall


%files
%gopkgfiles



%changelog
* Mon Nov  4 2019 ElXreno <elxreno@gmail.com>
- Initial packaging
