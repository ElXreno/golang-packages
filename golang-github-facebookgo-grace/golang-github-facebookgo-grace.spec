%global goipath         github.com/facebookgo/grace
%global commit          5729e484473f52048578af1b80d0008c7024089b
%global scm             git

%gometa

%global common_description %{expand:
A library that makes it easy to build socket based servers.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                A library that makes it easy to build socket based servers.

License:                MIT
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
